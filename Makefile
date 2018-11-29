
.PHONY: clean-pyc dist install-db start-dev test
.EXPORT_ALL_VARIABLES:
FLASK_ENV = development
FLASK_DEBUG = True

clean: clean-pyc
	rm	-rf dist .cache migrations drs.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name *pyc | grep __pycache__ | xargs rm -rf

start-dev:
	pip3 install -r requirements.txt
	flask run -h 0.0.0.0 -p 5000

install-db:
	python3 manage.py db init
	python3 manage.py db migrate
	python3 manage.py db upgrade

upgrade-db:
	python3 manage.py db migrate
	python3 manage.py db upgrade

test:
	pip3 install pytest==3.9.2
	py.test --verbose
