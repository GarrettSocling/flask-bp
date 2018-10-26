"""
Top level module of the flask-bp app.
"""
import sys
import yaml

from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# import strptime to avoid weird issues described @ http://bugs.python.org/msg221094
datetime.strptime('', '')

# Create WSGI app instance - this __name__.split('.') handles
# the case where the file is part of a package.
app = Flask(__name__.split('.')[0])

# to allow cross domain resource sharing over all domains,
# for more specific usage see @ https://github.com/corydolphin/flask-cors
CORS(app)

# load the configuration file
try:
    app_config = yaml.safe_load(open('etc/config.yml'))
except Exception as e:  # exceptions can be specific to the possible errors
    app.logger.error('exception encountered while parsing the configuration file, check the logs')
    app.logger.exception(e)
    sys.exit(1)

# when the file is loaded properly, load & set database configs for sqlalchemy
database_host = app_config['database']['host']
database_port = app_config['database']['port']
database_user = app_config['database']['user_name']
database_password = app_config['database']['password']
database_name = app_config['database']['database_name']

# setup database uri
# i used postgres as example database however any database can be used which is supported be sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://%s:%s@%s:%s/%s' % \
                                        (database_user, database_password, database_host,
                                         database_port, database_name)
# to suppress the track modification overhead warning and set it off
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(session_options={'autocommit': False})
db.init_app(app)
# import all the defined routes here
from app.api.v1 import *

# call register docs
register_routes_in_swagger()
