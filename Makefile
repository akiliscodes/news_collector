ENV_NAME := newscol
VENV_PATH := $(ENV_NAME)/bin/activate
PYTHON_VERSION := 3.9.6

define find.functions
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
endef

help:
	@echo 'The following commands can be used.'
	@echo ''
	$(call find.functions)

init:
	pip install uv
	uv venv -p $(PYTHON_VERSION) $(ENV_NAME)
	source $(VENV_PATH) && uv pip sync requirements.txt
