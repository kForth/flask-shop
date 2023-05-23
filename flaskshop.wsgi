# -*- coding: utf-8 -*-
"""Create an application instance."""

import sys
sys.path.insert(0, '/var/www/flask-shop')

activate_this = '/var/www/flask-shop/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from flaskshop.app import create_app

app = create_app()
