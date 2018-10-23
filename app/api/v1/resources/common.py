"""
Module for common resources.
"""
from flask_restful import Resource


class BaseRoutes(Resource):

    @staticmethod
    def get():
        return 'welcome'
