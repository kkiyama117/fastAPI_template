.PHONY : clean

# INSTALLER --------------------------------------------------------------------
init: install

install:
	python -m pip install -e .

## INSTALLER (dev) -------------------------------------------------------------
init_dev: install_dev post_install

install_dev:
	python -m pip install -U pip setuptools
	python -m pip install -r requirements.dev.txt

post_install:
	pre-commit install

# COMMANDS ----------------------------------------------------------------------
prod:
	docker-compose up --build

# DEV COMMANDS ------------------------------------------------------------------
start:
	uvicorn portfolio_api.app:app --reload

test:
	tox

format:
	black .

# CLEAN ------------------------------------------------------------------------
clean:
	@echo "TBD"

# Others -----------------------------------------------------------------------
overwrite_gitignore:
		 wget https://www.toptal.com/developers/gitignore/api/python,venv,visualstudiocode,pycharm+all,flask -O .gitignore
