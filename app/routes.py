import os
import flask

from flask import Blueprint, render_template, redirect

myroutes = Blueprint('simple_page', __name__, template_folder='templates')


image_directory = "/home/crayondata.com/sundararaman/Documents/arena/autotagging/engine"
static_image_route="/static/images/"
# STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), static_image_route)
# STATIC_PATH = os.path.join(image_directory, static_image_route)
STATIC_PATH=image_directory+static_image_route

print os.path.abspath(__file__)

@myroutes.route('/index')
def render_dashboard():
    return redirect('/dashboard')

@myroutes.route('/hello')
def hello():
    return 'Hello, World!'

@myroutes.route('/hello/<name>')
def hello_name(name):
    user = {'username': name}
    return render_template('index.html', user=user)

@myroutes.route('/<resource>')
def serve_static(resource):
	print STATIC_PATH, resource
	return flask.send_from_directory(STATIC_PATH, resource.strip())