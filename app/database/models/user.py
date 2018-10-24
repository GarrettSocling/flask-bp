"""
User model for user table in database.
"""
from app import db


class User(db.model):
    """Class for maintaining user table in the database."""
    __table_name__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50), nullable=False)
    user_name = db.Column(db.String(24), nullable=False)
    email_id = db.Column(db.String(120), nullable=False)
