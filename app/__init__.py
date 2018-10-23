"""
Top level module of the flask-bp app.
"""
from datetime import  datetime
from flask import Flask
from flask_cors import CORS

# import strptime to avoid weird issues described @ http://bugs.python.org/msg221094
datetime.strptime('', '')

# Create WSGI app instance - this __name__.split('.') handles
# the case where the file is part of a package.
app = Flask(__name__.split('.')[0])

# to allow cross domain resource sharing over all domains,
# for more specific usage see @ https://github.com/corydolphin/flask-cors
CORS(app)

# import all the defined routes here
from app.api.v1 import *
