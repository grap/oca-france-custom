.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT


DBNAME ?= oca-france-tests
MODULES ?= oca_france_all
DEMO_OPTION ?= "--demo"
ODOO_CONF ?=
PYTEST_OPTIONS ?= --ignore=./src/ .
TRANSLATE_MODULES ?= $(shell uv run manifestoo -d . list --separator , )

help: ## help
	uvx python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

setup-dev: ## Setup development environnement
	uv sync

update-db: ## Init or udpate database used by unittest (with demo data)
	uv run click-odoo-initdb ${ODOO_CONF} --unless-initialized -n "${DBNAME}" -m "${MODULES}" --no-cache ${DEMO_OPTION} --attachments-in-db --log-level info
	uv run click-odoo-update ${ODOO_CONF} -d "${DBNAME}"

translate-all: ## Generate/update translation files for all modules in this repository
	uv run click-odoo-makepot ${ODOO_CONF} --msgmerge --no-fuzzy-matching --purge-old-translations -d "${DBNAME}" -m ${TRANSLATE_MODULES}

test: ## Run unittest
	uv run pytest $(subst -c,--odoo-config,${ODOO_CONF}) --odoo-database="${DBNAME}" -c pyproject.toml ${PYTEST_OPTIONS}

run: ## Run Odoo
	uv run odoo ${ODOO_CONF} -d "${DBNAME}"
