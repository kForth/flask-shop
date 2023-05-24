# -*- coding: utf-8 -*-
"""Create an application instance."""
import os

DB_TYPE = "mysql"
DB_USER = "flaskshop"
DB_PASSWD = "flaskshop"
DB_NAME = "flaskshop"

os.environ['FLASK_SHOP_DB_TYPE'] = DB_TYPE
os.environ['FLASK_SHOP_DB_USER'] = DB_USER
os.environ['FLASK_SHOP_DB_PASSWD'] = DB_PASSWD
os.environ['FLASK_SHOP_DB_NAME'] = DB_NAME

from flaskshop.app import create_app

application = create_app()
