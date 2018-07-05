NBP README
==================

- cd <folder with development.ini/production.ini>

- $VENV/bin/pip install -e, instead you can use .whl package to install dependecies

- If there's NBP.sqlite, then ingore it. If there's not -> $VENV/bin/initialize_NBP_db development.ini

- $VENV/bin/pserve development.ini

