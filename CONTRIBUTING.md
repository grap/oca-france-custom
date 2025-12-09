# Contribute to the OCA France's Odoo instance

This guide aims to help happy volunteers to contribute to the OCA's Odoo instance.

It's split into 3 sections:

- [Concepts](#concepts): Main concepts to understand and general organization
- [Processes](#processes): Helping doing the work without missing crucial steps
- [HowTos](#howto): How to do specific tasks

## Concepts

This repository is setup as other OCA's repositories to launch CI as usual and as an
extra configuration in order to deploy the OCA France Odoo instance, as well as
facilitate the bootstrapping of a development environment.

Managing and freezing modules versions rely on python tools:

- [uv](https://docs.astral.sh/uv/)
- [hatch-odoo](https://pypi.org/project/hatch-odoo/)

### Hosting

Our Odoo instance is gracefully hosted by
[Auneor Conseil](https://www.auneor-conseil.fr) on dedicated LXD server responding to
[www.oca-france.fr](https://www.oca-france.fr).

## Processes

Here we focus on what to do without explaining how to do it.

### Release

There is nothing special to do more that make a commit publicly available.

While technically speaking there is nothing more than accessing to a public commit to
deploy a new version it's a common practice to merge your work on branch 18.0 before
deploying a new version in production.

> **Note**: in this repository we allow unreleased dependencies.

### deployment

Ask administrator to deploy the given commit.

## HowTos

Here we focus on how to do it, it's a suggest way to works but feel free to use your own
way.

We use `make` to ease some tasks described in the [Makefile](Makefile).

Global Makefile usage is as follow:

```bash
make <command> [PARAMETER=value] [...]
```

Parameters are optional and can be overriden (some are used by multiple commands):

- `DB_NAME`: database name (default: `oca-france-test`)
- `ODOO_CONF`: odoo configuration file (default: ``), example: `-c /path/to/odoo.conf`
- `DEMO_OPTION`: odoo demo option (default: `--demo`)
- `PYTEST_OPTIONS`: pytest options (default: `--ignore=./src/ .`)
- `TRANSLATE_MODULES`: modules to translate (default: all modules from this repository)
- `MODULES`: modules to install (default: `oca_france_all`)

Type `make help` to get a list of available commands.

### Setup developer environment

Requirements:

- Postgresql
- [uv](https://docs.astral.sh/uv/)
- Some dependencies to be able to build some python packages: `libpq-dev`,
  `build-essential`, TODO
- wkhtmltopdf

Prepare a python virtual environment with the correct python version (which uv will
download for you if necessary) and install the required dependencies:

```bash
make setup-dev
# or
uv sync
```

### Development

For addons living in this repository, you can just change code and restart Odoo with the
`uv run` command.

For addons in other repositories, the procedure is as follows:

- check out the repository somewhere, ie /src/\$repo
- add the following line to `pyproject.toml` in the `[tool.uv.sources]` section:

  ```pyproject
  odoo-addon-$youraddon = { path = "/srv/$repo/$youraddon", editable = true }
  ```

- run `uv sync`
- restart Odoo

### use unreleased dependency

There is two different goals:

- making the test CI pass: using regular test-requirements.txt files add a line such as

  ```requirements
  odoo-addon-res_company_mastodon_link @ git+https://github.com/OCA/social@refs/pull/1754/head#subdirectory=res_company_mastodon_link
  ```

- bring the unreleased dependency in the uv project (and the built docker image), add
  the following line to `pyproject.toml` in the `[tool.uv.sources]` section:

  ```pyproject
  odoo-addon-res_company_mastodon_link = {
    git = "https://github.com/OCA/social",
    rev = "refs/pull/1754/head",
    subdirectory = "res_company_mastodon_link"
  }
  ```

### Initialized or update Odoo database

You can use the `make update-db` command to initialized or update the database.
optionnaly you can set the `DB_NAME` environment variable to specify the database name
and a `ODOO_CONF` to specify how to connect to the database.

```bash
make update-db [DB_NAME=oca-france-test] [ODOO_CONF=-c /path/to/odoo.conf] [DEMO_OPTION=]
```

or do it manually:

```bash
export DB_NAME=oca-france-test
uv run click-odoo-initdb --unless-initialized \
   -n "$DB_NAME" -m oca_france_all --no-cache [--demo]
uv run click-odoo-update --if-exists -d "$DB_NAME" --i18n-overwrite
```

### Setup database and launch tests

- setup/update database **with demo data** (cf
  [previous paragraph: Initialized or update Odoo database](#initialized-or-update-odoo-database)
  )
- run tests using pytest launcher

```bash
make test
# or
uv run pytest --odoo-database oca-france --cov ./oca_france_membership/ ./oca_france_membership/
```

### Update OCB Branch

```bash
uv sync -P odoo
```

### Update a specific OCA module dependency using the latest pypi release

```bash
uv sync -P odoo-addon-<module-name>
```

### Bump all dependencies to the latest version

```bash
uv sync -U
```
