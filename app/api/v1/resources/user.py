"""
Module for user resource.
"""
import json

from app import app
from flask import Response, request
from flask_restful import Resource

from app.database.models.user import User
from app.api.v1.schemas.users import UserArgs, UserResponse


class Users(Resource):
    """Class for handling user resources."""

    def get(self):
        """GET method handler."""
        user_id = request.args.get('user_id')
        user = User()
        return Response(json.dumps(UserResponse().dump(user.get(user_id)).data),
                        status=200, mimetype='application/json')

    def post(self):
        """POST method handler."""
        user_data = json.loads(request.data.decode('utf-8'))
        try:
            user = User(full_name=user_data.get('full_name'),
                        user_name=user_data.get('user_name'),
                        email_id=user_data.get('email_id'))
            user.add()
            return Response(json.dumps({'message': 'user {0} added successfully'.format(user_data.get('user_name'))}),
                            status=200, mimetype='application/json')
        except Exception as e:
            app.logger.error('exception encountered')
            app.logger.exception(e)
            return Response(json.dumps({'message': 'user {0} addition failed'.format(user_data.get('user_name'))}),
                            status=500, mimetype='application/json')
