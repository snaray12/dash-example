import os
from flask import Flask

from app.routes import myroutes

from app.layouts import mylayout

server = Flask(__name__)

server.config.from_object(os.environ['APP_SETTINGS'])

server.register_blueprint(myroutes)
