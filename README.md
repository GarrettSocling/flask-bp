# flask-bp
**flask-bp** is a comprehensive flask boilerplate for prototyping. It includes most
common aspects of the projects such as Database migrations, resourceful routing, unit-testing
and many more.

**[flask-restful](https://flask-restful.readthedocs.io/en/latest/)** has been used for resourceful routing in api server.
**[Flask-cors](https://github.com/corydolphin/flask-cors)** has been used to manage the Cross-Origin Resource sharing.
**[Marshmallow Python](https://github.com/marshmallow-code/marshmallow)** has been used for data management in api 
requests and responses.
**[Flask SQLAlchemy](https://github.com/mitsuhiko/flask-sqlalchemy)** has been used for database modeling.
**[Flask Script 2.0.6 (deprecated)](https://github.com/smurfix/flask-script) & 
[Flask Migrate 2.3.0](https://github.com/miguelgrinberg/Flask-Migrate)** has been used for database migrations.
**[apispec 0.39.0](https://github.com/marshmallow-code/apispec) &
[flask-apispec 0.7.0](https://github.com/jmcarp/flask-apispec)** has been used for auto swagger documentation of the apis.

## Setup
A virtual environment should be used, e.g
```bash
virtualenv flaskbp-env
``` 
Activate the virtual environment and install the requirements:
```bash
source flaskbp-env/bin/activate
pip install -r requirements.txt
```
Run the flask-bp:
```bash
python run.py
```

### Database Migrations
To initialize  database migrations
```bash
python manage.py db init
```
To migrate the database
```bash
python manage.py db migrate
```
To upgrade the database
```bash
python manage.py db upgrade
```

## Open Source Resources Used
1. [Python 3.7](https://www.python.org/downloads/release/python-370/)
2. [Flask 1.0.2](https://github.com/pallets/flask)
3. [Flask-Restful 0.3.6](https://flask-restful.readthedocs.io/en/latest/)
4. [Flask-cors 3.0.6](https://github.com/corydolphin/flask-cors)
5. [Marshmallow Python 2.16.1](https://github.com/marshmallow-code/marshmallow)
6. [Flask SQLAlchemy 2.3.2](https://github.com/mitsuhiko/flask-sqlalchemy)
7. [PyYAML 3.13](https://github.com/yaml/pyyaml)
8. [Flask Script 2.0.6 (deprecated)](https://github.com/smurfix/flask-script)
9. [Flask Migrate 2.3.0](https://github.com/miguelgrinberg/Flask-Migrate)
10. [apispec 0.39.0](https://github.com/marshmallow-code/apispec)
11. [flask-apispec 0.7.0](https://github.com/jmcarp/flask-apispec)
