# flask-bp
**flask-bp** is a comprehensive flask boilerplate for prototyping. It includes most
common aspects of the projects such as Database migrations, resourceful routing, unit-testing
and many more.

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
