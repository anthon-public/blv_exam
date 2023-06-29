.PHONY: clean-pyc clean-build help

halabasterelp:
	@perl -nle'print $& if m{^[a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-25s\033[0m %s\n", $$1, $$2}'

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

lint: isort black flake8

flake8:
	python -m flake8 app tests

isort:
	isort app tests

black:
	black app tests -l 79

test:
	pytest --tb=short -q -s -rw app tests

coverage:
	pytest --tb=short -q -s -rw --cov=app app tests

install:
	pip install -r requirements/base.txt
	pip install -r requirements/dev.txt
	pip install -r requirements/test.txt
