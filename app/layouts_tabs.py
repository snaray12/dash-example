import dash_html_components as html
import dash_core_components as dcc
import dash_table_experiments as dt
# import dash_table
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

tab_parent = {
	'width':'95%',
	'margin':'2.5%',
	# 'margin-right':'2.5%',
}

tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}

mylayout = html.Div(children=[
	html.Div([
		html.Img(src="/crayon_logo_400x400.jpg",
			style={"width":"40px", "height":"40px", "float":"left"}
			),
		html.H1(children='Automatic tag extraction engine',
    	style={
            'textAlign': 'center',
            'color': colors['text'],
            'float':'left',
            'padding-left':'10%',
            'padding-top':'5px'
        }),
        ], style=tabs_styles),
	html.Div([
		dcc.Tabs(id="tabs-pane", value='tab-1-pane', children=[
			dcc.Tab(label='Tagging', value='tab-1-pane', style=tab_style, selected_style=tab_selected_style),
			dcc.Tab(label='Recommendation', value='tab-2-pane', style=tab_style, selected_style=tab_selected_style),
			], style=tabs_styles), 
	html.Div(id='tabs-content-pane')
		], style=tab_parent),
    html.Div([dt.DataTable(
        # Initialise the rows
        rows=[{}],
        row_selectable=False,
        filterable=False,
        sortable=True,
        selected_row_indices=[],
        id='table1',
    )], style={'display':'none'}, id="table1-id"),
    html.Div([dt.DataTable(
        # Initialise the rows
        rows=[{}],
        row_selectable=False,
        filterable=False,
        sortable=True,
        selected_row_indices=[],
        id='table2',
    )], style={"display":"None"}, id="table2-id"),
    ])


tab1_layout = html.Div([
    html.Div([
            dcc.Textarea(
                id="txtarea",
                placeholder='Enter a value...',
                value='This is a TextArea component',
                style={'width': '60%', 'height':'10%', 'float':'left', 'margin-left':'10%', 'margin-right':'5%', 'margin-bottom':'2%'}
                ),
            html.Button('Submit', id='button', style={'margin-top':'1%'})
        ],
        style={'width':'100%', 'float':'left'})
])

tab2_layout = html.Div([
    dcc.Dropdown(
        id="hotel-dropdown",
        options=[
        {'label':'Hotel 1', 'value':"hot1"},
        {'label':'Hotel 2', 'value':"hot2"}, 
        {'label':'Hotel 3', 'value':"hot3"}],
        value="hot2"
        ),
    # html.Div(id='my-div')
    # dt.DataTable(
    #     # Initialise the rows
    #     rows=[{}],
    #     row_selectable=False,
    #     filterable=False,
    #     sortable=True,
    #     selected_row_indices=[],
    #     id='table',
    # ),
])