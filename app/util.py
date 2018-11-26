import spacy

from gensim.corpora import Dictionary
from gensim.models import TfidfModel

import pandas as pd


class TextProcessor:

	def load_dict(self):
		if self.dictionary:
			return self.dictionary
		else:
			self.dictionary = Dictionary.load(self.dict_file)
			return self.dictionary
		return self.dictionary

	def load_tfidf_model(self):
		return TfidfModel.load(self.model_file)
 
	def __init__(self, name):
		self.name = name
		self.nlp = spacy.load('en_core_web_sm')
		self.dict_file = 'similarity_dictionary.dict'
		self.model_file = 'tfidf.model'
		self.stoplist = ['you', 'Rooms', 'yourself', 'home', 'advantage', 'Premium_Amenities', 'Additional_features', 'distance','close_proximity', 'Conveniences', 'phones', 'Rec', 'comfort', 'style', 'guests', 'the_feel','it', 'the_centre', 'its_state', 'mind', 'everyone', 'colour', 'its_smell', 'Diesel', 'your_every_wish','Pictures', 'the_perfect_mix', 'the_lobby', 'Alternative_service', 'the_rooms', 'the_city', 'the_heart','charge', 'renovation', 'iron_gate', 'its_original_facade', 'its_owners', 'collectors', 'a_place', 'the_trade', 'the_rhythm', 'its_citizens', 'they', 'day', 'any_time', 'a_treat', 'a_stay', 'name','location', 'Property_Location', 'use', 'convenient_amenities', 'two_buildings', 'Modern', 'Attentive_service', 'the_greatest_movie_stars', 'your_well-being', 'the_view', 'the_hotel','a_fee', 'This_hotel', 'the_air', 'an_era', 'the_details', 'The_hotel', 'minutes', 'we', 'this_wifi', 'one', 'hotel', 'the_option', 'them', 'themselves', 'different_categories', 'comforts','the_importance', 'the_team', 'proactivity', 'a_wide_range', 'guest', 'I']
		self.dictionary = None
		self.model = self.load_tfidf_model()
        
	def remove_br(self,text):
	    desc = text.replace(" <br/>", ": ").replace("<br/ ", '')
	    return desc

	def get_noun_list(self,text):
	    doc = self.nlp(text.decode('utf-8'))
	    nc = []
	    for np in doc.noun_chunks:
	        txt = np.text.replace(' ','_').replace('<br/>','').replace('<br/', '').lower()
	        if not txt in self.stoplist:
	        	print "Adding : %s" %(txt)
	        	nc.append(txt)
	        else:
	            print "Ignoring: ", txt
	    return nc

	def get_doc2bow(self,text_list):
		dictionary = self.load_dict()
		initial_len = len(dictionary)
		corpus = [dictionary.doc2bow(text, allow_update=True) for text in text_list]
		final_len = len(dictionary)
		if initial_len != final_len:
			dictionary.save(self.dict_file)
		return corpus

	def fit_tfidf_model(self,corpus):
		dictionary = self.load_dict()
		corpus_tfidf = self.model[corpus]
		test_corpus_list = []
		for idx, doc_lst in enumerate(corpus_tfidf):
			for kw, wt in doc_lst:
				print kw, wt
				mydict = {"Keyword":dictionary[kw], "Weight":wt}
				test_corpus_list.append(mydict)
		test_corpus_df = pd.DataFrame(test_corpus_list)
		# test_corpus_df.sort_values(by=['Weight'], ascending=False, inplace=True)
		return test_corpus_df

	def get_stats(self, text):
		cleaned_text = self.remove_br(text)
		doc = self.nlp(cleaned_text.decode('utf-8'))
		sentences = [sent.string.strip() for sent in doc.sents]
		words = [w.string.strip() for w in doc]
		lemma_norm_words = [w.lemma_ for w in doc if not w.is_stop and not w.is_punct]
		return len(sentences), len(words), len(set(lemma_norm_words))

	def process(self,text):
		cleaned_text = self.remove_br(text)
		noun_list = self.get_noun_list(cleaned_text)
		d2b = self.get_doc2bow([noun_list])
		d2b_tfidf_fitted = self.fit_tfidf_model(d2b)
		return d2b_tfidf_fitted.sort_values(by=['Weight'], ascending=False, inplace=False)