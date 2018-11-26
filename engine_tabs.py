import os

import flask
import dash
import dash_table
import dash_table_experiments as dt
import dash_html_components as html

from app.flask_server import server

from app.layouts import mylayout, tab1_layout
# from app.new_layouts import mylayout
from app.util import TextProcessor

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" ]

app = dash.Dash(__name__, server=server, url_base_pathname='/dashboard/', \
    external_stylesheets=external_stylesheets, assets_url_path="/static/css/styles.css")

app.layout = mylayout
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

# @app.callback(
    # dash.dependencies.Output('output-container-button', 'children'),
    # dash.dependencies.Output('table', 'rows'),
    # [dash.dependencies.Input('button', 'n_clicks')],
    # [dash.dependencies.State('txtarea', 'value')])
def update_output(value):
    print value
    tp = TextProcessor("temp")
    result = tp.process(value)
    sent_len, word_len, norm_word_len = tp.get_stats(value)
    print sent_len, word_len, norm_word_len
    print result
    return result.to_dict('records')

@app.callback(
    dash.dependencies.Output('output-container-button', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('txtarea', 'value')])
def update_stats(n_clicks, value):
    tp = TextProcessor("temp")
    result = tp.process(value)
    sent_len, word_len, norm_word_len = tp.get_stats(value)
    print sent_len, word_len, norm_word_len
    return html.Div(children="Length of sentence '{}', Length of word '{}', Length of normalized word '{}'".format(sent_len, word_len, norm_word_len),
        style={'width':'100%', 'float':'left'})
    # return "Length of sentence '{}', Length of word '{}', Length of normalized word '{}'".format(sent_len, word_len, norm_word_len)

@app.callback(dash.dependencies.Output('tabs-content-pane', 'children'),
              [dash.dependencies.Input('tabs-pane', 'value')],
              [dash.dependencies.State('txtarea', 'value')])
def render_content(tab, value):
    if tab == 'tab-1-pane':
        return update_stats(1,value)
    elif tab == 'tab-2-pane':
        return update_output(value)


if __name__ == '__main__':
    app.run_server(debug=True, port=8050, host='127.0.0.1')
    app.run_server(debug=True)