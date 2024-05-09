# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from os import environ
from pathlib import Path
import yaml

PERSISTENCE_PATH = r'/opt/fts'
YAML_PATH = f"{PERSISTENCE_PATH}/FTSConfig.yaml"


class Config(object):
    basedir = Path(__file__).parent.absolute()
    purelib_path = basedir.parent

    with open(YAML_PATH, "r") as stream:
        config_yaml = yaml.safe_load(stream)
        if config_yaml is None:
            config_yaml = {}

    SECRET_KEY = 'key'

    # This will connect to the FTS db
    SQLALCHEMY_DATABASE_URI = environ.get('FTS_UI_SQLALCHEMY_DATABASE_URI',
                                          config_yaml.get('SQLALCHEMY_DATABASE_URI',
                                                          'sqlite:///' + '/opt/fts/FTSServer-UI.db'))

    # certificates path
    # cert_path = Path("/opt/fts.venv/lib/python3.11/site-packages/FreeTAKServer/certs/")
    # or platform independently
    # cert_path = purelib_path / 'FreeTAKServer' / 'certs'

    # crt file path
    # crtfilepath = str(cert_path / "pubserver.pem")

    # key file path
    # keyfilepath = str(cert_path / "pubserver.key.unencrypted")

    # this IP will be used to connect with the FTS API
    IP = environ.get('FTS_IP', config_yaml.get('FTS_IP', '127.0.0.1'))

    # Port the UI uses to communicate with the API
    PORT = environ.get('FTS_API_PORT', config_yaml.get('FTS_API_PORT',  '19023'))

    # Protocol the UI uses to communicate with the API
    PROTOCOL = environ.get('FTS_API_PROTO', config_yaml.get('FTS_API_PROTO', 'http'))

    # the public IP your server is exposing
    APPIP = environ.get('FTS_UI_EXPOSED_IP', config_yaml.get('FTS_UI_EXPOSED_IP', '127.0.0.1'))

    # webmap IP
    WEBMAPIP = environ.get('FTS_MAP_EXPOSED_IP', config_yaml.get('FTS_MAP_EXPOSED_IP', '127.0.0.1'))

    # webmap port
    WEBMAPPORT = int(environ.get('FTS_MAP_PORT', config_yaml.get('FTS_MAP_PORT', 8000)))

    # webmap protocol
    WEBMAPPROTOCOL = environ.get('FTS_MAP_PROTO', config_yaml.get('FTS_MAP_PROTO', 'http'))

    # this port will be used to listen
    APPPort = int(environ.get('FTS_UI_PORT', config_yaml.get('FTS_UI_PORT', 5000)))

    # the webSocket key used by the UI to communicate with FTS.
    WEBSOCKETKEY = environ.get('FTS_UI_WSKEY', config_yaml.get('FTS_UI_WSKEY', 'YourWebsocketKey'))

    # the API key used by the UI to communicate with FTS.
    # generate a new system user and then set it.
    APIKEY = environ.get('FTS_API_KEY', config_yaml.get('FTS_API_KEY', 'Bearer token'))

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

    cy = Config.config_yaml

    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
        environ.get('APPSEED_DATABASE_USER', cy.get('APPSEED_DATABASE_USER', 'appseed')),
        environ.get('APPSEED_DATABASE_PASSWORD', cy.get('APPSEED_DATABASE_PASSWORD', 'appseed')),
        environ.get('APPSEED_DATABASE_HOST', cy.get('APPSEED_DATABASE_HOST', 'db')),
        environ.get('APPSEED_DATABASE_PORT', cy.get('APPSEED_DATABASE_PORT', 5432)),
        environ.get('APPSEED_DATABASE_NAME', cy.get('APPSEED_DATABASE_NAME', 'appseed'))
    )


class DebugConfig(Config):
    DEBUG = True


config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}
