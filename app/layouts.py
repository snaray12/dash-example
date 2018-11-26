import dash_html_components as html
import dash_core_components as dcc
import dash_table_experiments as dt

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

myclass = {
	'padding-left':'20%'
}

markdown_text = '''
# One Hash
## Two Hash
### Dash and Markdown
#### Four Hash
##### 5 Hash
_underscore_
*star*
__double underscore__
Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''

mylayout = html.Div(children=[
	html.Div([
		html.Img(src="/crayon_logo_400x400.jpg",
			style={"width":"60px", "height":"60px", "float":"left"}
			),
		html.H1(children='Automatic tag extraction engine',
    	style={
            'textAlign': 'center',
            'color': colors['text'],
            'float':'left',
            'padding-left':'10%',
            'padding-top':'5px'
        })]),
    html.Div([
    	# dcc.Checklist(
    	# 	options=[
    	# 	{'label': 'New York City', 'value': 'NYC'},
    	# 	{'label': 'Montreal', 'value': 'MTL'},
    	# 	{'label': 'San Francisco', 'value': 'SF'}
    	# 	],
    	# 	values=['MTL', 'SF'],
    	# 	style={"width":'30%;', 'float':'left'}
    	# 	),
    	dcc.Textarea(
    		id="txtarea",
    		placeholder='Enter a value...',
    		value='This is a TextArea component',
    		style={'width': '60%', 'height':'10%', 'float':'left', 'margin-left':'10%', 'margin-right':'5%', 'margin-bottom':'2%'}
    		),
    	html.Button('Submit', id='button', style={'margin-top':'1%'})
    	],
    	style={'width':'100%', 'float':'left'}),
    dt.DataTable(
    # Initialise the rows
    rows=[{}],
    row_selectable=False,
    filterable=False,
    sortable=True,
    selected_row_indices=[],
    id='table',
    min_width=555,
    min_height=400,
    # class_name="myclass",
    # style={'width':'80%', 'float':'left', 'display':'inline-block'}
    ),
    html.Div(id='output-container-button',
             children='Enter a value and press submit',
             style={'width':'100%', 'float':'left'})




    # dash_table.DataTable(
    #     id='table',
    #     columns=[{"name": i, "id": i} for i in result.columns],
    #     data=result.to_dict("rows")
    #     )
    # html.Div(children='''
    #     Dash: A web application framework for Python.
    # '''),
    # dcc.Markdown(children=markdown_text)
    ])