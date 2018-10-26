
.PHONY: clean-pyc dist install-db start-dev

clean: clean-pyc
	rm	-rf dist .cache migrations drs.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name *pyc | grep __pycache__ | xargs rm -rf

start-dev:
	pip3 install -r requirements.txt
	python run.py

install-db:
	python3 manage.py db init
	python3 manage.py db migrate
	python3 manage.py db upgrade

upgrade-db:
	python3 manage.py db migrate
	python3 manage.py db upgrade