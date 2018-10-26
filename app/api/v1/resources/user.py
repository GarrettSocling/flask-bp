"""
Module for user resource.
"""
import json

from flask import Response, request
from flask_restful import Resource

from app.database.models.user import User


class Users(Resource):
    """Class for handling user resources."""

    def get(self):
        """GET method handler."""
        user_id = request.args.get('user_id')
        user = User()
        print(user.get(user_id))
        return Response(json.dumps({'messgae': 'user route GET'}), status=200, mimetype='application/json')

    def post(self):
        """POST method handler."""
        print(request.data)
        return 'abcd'
