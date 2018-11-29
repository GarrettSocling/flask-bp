import json


def test_common_api(flask_app):
    expected_response = {'message': 'flask-bp API Version 1.0',
                         'method': 'GET',
                         'route_path': 'api/v1/'}
    rv = flask_app.get('api/v1/')
    assert rv.status_code == 200
    data = json.loads(rv.data.decode('utf-8'))
    assert data == expected_response
