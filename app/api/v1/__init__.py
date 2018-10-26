"""
Top level modules for the routes of flask-bp api version 1.0 routes.
"""
from app import app
from flask_restful import Api

from app.api.v1.resources.common import BaseRoutes
from app.api.v1.resources.user import Users

# initialize flask-restful api instance
# for more details see @ https://flask-restful.readthedocs.io/en/latest/
api = Api(app, prefix='/api/v1')

# add a resource
# noinspection PyTypeChecker
api.add_resource(BaseRoutes, '/')
api.add_resource(Users, '/user')
