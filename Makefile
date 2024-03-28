.ONESHELL:

ENV_NAME = ./newscol
VENV_PATH = $(ENV_NAME)/bin/activate
PYTHON_VERSION = 3.9.6

.PHONY: init run clean

init:
	pip install uv
	uv venv -p $(PYTHON_VERSION) $(ENV_NAME)
	. $(VENV_PATH) && uv pip install -r requirements.txt

run: init
	$(ENV_NAME)/bin/python src/main.py 

clean:
	rm -rf $(ENV_NAME)