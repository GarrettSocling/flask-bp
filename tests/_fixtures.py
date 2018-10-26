"""
fixtures module
"""
import pytest


@pytest.fixture()
def flask_app():
    """flask app fixture."""
    from app import app
    app.testing = True
    app.debug = False
    client = app.test_client()
    ctx = app.test_request_context()
    ctx.push()
    yield client
    ctx.pop()
