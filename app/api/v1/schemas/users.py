"""
Schemas for user models.
"""
from marshmallow import fields, Schema


class UserResponse(Schema):
    """Response schema for user model."""
    full_name = fields.String(required=True)
    user_name = fields.String(required=True)
    email_id = fields.String(required=True)


class UserArgs(Schema):
    """Request/Args schema for user model."""
    full_name = fields.String(required=True)
    user_name = fields.String(required=True)
    email_id = fields.String(required=True)
