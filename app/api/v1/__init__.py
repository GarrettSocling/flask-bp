"""
Top level modules for the routes of flask-bp api version 1.0 routes.
"""
from app import app
from flask_restful import Api

from app.common.swagger_docs import SwaggerDocs
from app.api.v1.resources.common import BaseRoutes
from app.api.v1.resources.user import Users

# initialize flask-restful api instance
# for more details see @ https://flask-restful.readthedocs.io/en/latest/
api = Api(app, prefix='/api/v1')
swagger = SwaggerDocs(app, 'v1')

# add a resource
# noinspection PyTypeChecker
api.add_resource(BaseRoutes, '/')
api.add_resource(Users, '/user')

# init swagger docs
swagger_docs = swagger.init_docs()


def register_routes_in_swagger():
    """Method to register routes into swagger docs."""
    for route in [Users]:
        swagger_docs.register(route)
