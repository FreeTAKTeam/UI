# -*- encoding: utf-8 -*-

import os
from   os import environ

class Config(object):

    basedir    = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = 'YourSecretKey'

    # This will connect to the FTS db
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + '/opt/FTSServer-UI.db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + '/opt/fts/FTSServer-UI.db'

    # certificates path
    # certpath = "/usr/local/lib/python3.8/dist-packages/FreeTAKServer/certs/"
    certpath = "/opt/fts/certs/"

    # crt file path
    #crtfilepath = f"{certpath}pubserver.pem"
    crtfilepath = f"{certpath}server.pem"

    # key file path
    #keyfilepath = f"{certpath}pubserver.key.unencrypted"
    keyfilepath = f"{certpath}server.key.unencrypted"

    # Protocol the UI uses to communicate with the API
    PROTOCOL = "http"

    # this IP will be used to connect with the FTS API
    # IP = '127.0.0.1'
    IP = 'fts'

    # Port the  UI uses to communicate with the API
    PORT = '19023'

    # the public IP your server is exposing
    # APPIP = '127.0.0.1'
    APPIP = '0.0.0.0'

    # webmap IP
    WEBMAPIP = "127.0.0.1"
    # WEBMAPIP = "0.0.0.0"

    # webmap port
    WEBMAPPORT = 8000

    # webmap protocol
    WEBMAPPROTOCOL = 'http'

    # this port will be used to listen
    APPPort = 5000

    # the webSocket  key used by the UI to communicate with FTS.
    WEBSOCKETKEY = 'WebSocketKey'

    # the API key used by the UI to comunicate with FTS. generate a new system user and then set it
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