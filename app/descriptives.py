import pandas as pd
import numpy as np
import os
import time
import spacy

def get_summary(file):
	nlp = spacy.load('en_core_web_sm')
	df = pd.read_csv(file, sep="\t", encoding='utf-8')
	print df.shape
	print df.dtypes
	
	z_summary = df['Summary'].tolist()
	z_sent_count = []
	z_word_count = []
	z_stopfree_word_count = []
	for desc in z_summary:
		doc = nlp(desc)
		sent_len = len(list(doc.sents))
		# print sent_len
		z_sent_count.append(sent_len)
		sent_w_len = []
		sent_w_len_normalized = []
		for sent in doc.sents:
			doc2 = nlp(sent.text)
			w_len = len(list(doc2))
			# print w_len
			sent_w_len.append(w_len)
			w_len_norm = len([w for w in doc2 if not w.is_alpha and not w.is_stop])
			sent_w_len_normalized.append(w_len_norm)
		z_word_count.append(sent_w_len)
		z_stopfree_word_count.append(sent_w_len_normalized)
	df['z_sent_count'] = z_sent_count
	df['z_word_count'] = z_word_count
	df['z_stopfree_wc'] = z_stopfree_word_count

	print z_sent_count, z_word_count, z_stopfree_unique_word_count
	return df


if __name__ == '__main__':
	path = os.path.dirname(os.path.abspath( __file__ ))
	file = 'input.tsv'
	print os.path.join(path, file)
	df = get_summary(os.path.join(path,file))
	timestr = time.strftime("%Y%m%d_%H%M%S")
	df.to_csv("input_"+timestr+'.tsv')