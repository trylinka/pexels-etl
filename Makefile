# Makefile variables
VENV_NAME ?= venv_etl

# Setup environment for ETL
.PHONY: setup_python
setup_python:
	rm -rf $(VENV_NAME)
	python3 -m venv $(VENV_NAME)
	$(VENV_NAME)/bin/pip3 install -r requirements.txt

# Setup database with tables
.PHONY: setup_db
setup_db:
	rm -f pexels_photos.db
	$(VENV_NAME)/bin/python3 -m pexels_etl.setup_db

# Run ETL process
.PHONY: run_etl
run_etl: setup_python setup_db
	$(VENV_NAME)/bin/python3 -m pexels_etl

# Execute demo queries
.PHONY: demo
demo:
	$(VENV_NAME)/bin/python3 -m pexels_etl.demo

# Build the whole pipeline
.PHONY: all
all: run_etl demo
