# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

import os
from os import environ
# from sysconfig import get_path
from pathlib import Path


class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    # purelib_path = Path(get_path('purelib'))
    purelib_path = Path(basedir).parent

    SECRET_KEY = 'key'

    # This will connect to the FTS db
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + '/opt/FTSServer-UI.db'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' +
    #               str(purelib_path / 'FreeTAKServer' / 'FTSDataBase.db')

    # experimental SSL support in the UI

    # certificates path
    # cert_path = Path("/usr/local/lib/python3.8/dist-packages/FreeTAKServer/certs/")
    # or platform independently
    # cert_path = purelib_path / 'FreeTAKServer' / 'certs'

    # crt file path
    # crtfilepath = str(cert_path / "pubserver.pem")

    # key file path
    # keyfilepath = str(cert_path / "pubserver.key.unencrypted")

    # this IP will be used to connect with the FTS API
    IP = '127.0.0.1'

    # Port the UI uses to communicate with the API
    PORT = '19023'

    # Protocol the UI uses to communicate with the API
    PROTOCOL = 'http'

    # the public IP your server is exposing
    APPIP = '127.0.0.1'

    # webmap IP
    WEBMAPIP = '127.0.0.1'

    # webmap port
    WEBMAPPORT = 8000

    # webmap protocol
    WEBMAPPROTOCOL = 'http'

    # this port will be used to listen
    APPPort = 5000

    # the webSocket key used by the UI to communicate with FTS.
    WEBSOCKETKEY = 'YourWebsocketKey'

    # the API key used by the UI to communicate with FTS.
    # generate a new system user and then set it.
    APIKEY = 'Bearer token'

    # For 'in memory' database, please use:
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # THEME SUPPORT
    #  if set then url_for('static', filename='', theme='')
    #  will add the theme name to the static URL:
    #    /static/<DEFAULT_THEME>/filename
    # DEFAULT_THEME = "themes/dark"
    DEFAULT_THEME = None


class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
        environ.get('APPSEED_DATABASE_USER', 'appseed'),
        environ.get('APPSEED_DATABASE_PASSWORD', 'appseed'),
        environ.get('APPSEED_DATABASE_HOST', 'db'),
        environ.get('APPSEED_DATABASE_PORT', 5432),
        environ.get('APPSEED_DATABASE_NAME', 'appseed')
    )


class DebugConfig(Config):
    DEBUG = True


config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}