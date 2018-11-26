import os
import pandas as pd
import numpy as np

import flask
import dash
import dash_table
import dash_table_experiments as dt
import dash_html_components as html

from app.flask_server import server

from app.layouts_tabs import mylayout, tab1_layout,tab2_layout
# from app.new_layouts import mylayout
from app.util import TextProcessor

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" ]

app = dash.Dash(__name__, server=server, url_base_pathname='/dashboard/', \
    external_stylesheets=external_stylesheets, assets_url_path="/static/css/styles.css")

app.layout = mylayout
app.config['suppress_callback_exceptions']=True

image_directory = "/home/crayondata.com/sundararaman/Documents/arena/autotagging/engine"
static_image_route="/static/images/"
STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), static_image_route)


@app.server.route('/static/<resource>')
def serve_static(resource):
    return flask.send_from_directory(STATIC_PATH, resource)

# Add a static image route that serves images from desktop
# Be *very* careful here - you don't want to serve arbitrary files
# from your computer or server
@app.server.route('{}<image_path>'.format(static_image_route))
def serve_image(image_path):
    image_name = '{}'.format(image_path)
    if image_name not in list_of_images:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory, image_name)

@app.callback(
#     dash.dependencies.Output('output-container-button', 'children'),
    dash.dependencies.Output('table1', 'rows'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('txtarea', 'value')])
def update_output(n_clicks, value):
    print value
    tp = TextProcessor("temp")
    result = tp.process(value)
    sent_len, word_len, norm_word_len = tp.get_stats(value)
    print sent_len, word_len, norm_word_len
    print result
    return result.to_dict('records')

@app.callback(
#     dash.dependencies.Output('output-container-button', 'children'),
    dash.dependencies.Output('table2', 'rows'),
    [dash.dependencies.Input('hotel-dropdown', 'value')])
def update_recommendations(value):
    print value
    tp = TextProcessor("temp")
    return tp.get_recommendations(value).to_dict('result')
    # return tp.get_recommendations(value)

# @app.callback(
#     dash.dependencies.Output('output-container-button', 'children'),
#     [dash.dependencies.Input('button', 'n_clicks')],
#     [dash.dependencies.State('txtarea', 'value')])
def update_stats(n_clicks, value):
    tp = TextProcessor("temp")
    result = tp.process(value)
    sent_len, word_len, norm_word_len = tp.get_stats(value)
    print sent_len, word_len, norm_word_len
    return html.Div(children="Length of sentence '{}', Length of word '{}', Length of normalized word '{}'".format(sent_len, word_len, norm_word_len),
        style={'width':'100%', 'float':'left'})
    # return "Length of sentence '{}', Length of word '{}', Length of normalized word '{}'".format(sent_len, word_len, norm_word_len)

@app.callback(dash.dependencies.Output('tabs-content-pane', 'children'),
              [dash.dependencies.Input('tabs-pane', 'value')])
def render_content(tab):
    print tab
    if tab == 'tab-1-pane':
        return tab1_layout
    elif tab == 'tab-2-pane':
        return tab2_layout

@app.callback(dash.dependencies.Output('hotel-dropdown', 'options'),
              [dash.dependencies.Input('tabs-pane', 'value')])
def load_options(tab):
    tp = TextProcessor('test')
    return tp.get_hotel_list()

@app.callback(dash.dependencies.Output('table1-id', 'style'),
              [dash.dependencies.Input('tabs-pane', 'value')])
def show_hide_table1(tab):
    return _show_hide_style_switch_(tab, 'tab-1-pane')

@app.callback(dash.dependencies.Output('table2-id', 'style'),
              [dash.dependencies.Input('tabs-pane', 'value')])
def show_hide_table1(tab):
    return _show_hide_style_switch_(tab, 'tab-2-pane')

def _show_hide_style_switch_(tab, expected):
    if tab == expected:
        return {'display':'block'}
    else:
        return {'display':'none'}

# @app.callback(dash.dependencies.Output('table2', 'rows'),
#     [dash.dependencies.Input('hotel-dropdown', 'value')])
# def update_selection(choice):
#     print choice
#     df = pd.DataFrame({'Column {}'.format(i): np.random.rand(50) + i*10 for i in range(6)})
#     return df.to_dict('records')

if __name__ == '__main__':
    app.run_server(debug=True, port=8050, host='127.0.0.1')
    app.run_server(debug=True)
