all: clean-pyc test

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

lines:
	find . -name "*.py"|xargs cat|wc -l

test:
	@py.test -vv --tb=short --ds=tests.test_settings --nomigrations tests

flake8:
	@flake8 --ignore=E501,F401,W292 hammer-api tests scripts