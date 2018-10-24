"""
flask-bp package for the database models.
"""
from flask_sqlalchemy import declarative_base

__all__ = ['user']

from app.database.models import *
