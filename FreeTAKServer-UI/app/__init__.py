# -*- encoding: utf-8 -*-
"""
License: EPL
Copyright (c) 2021 - present FTS team
go to line 77+ for configuring the FTS UI
"""

from flask import Flask, url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils.functions import database_exists
from importlib import import_module
from logging import basicConfig, DEBUG, getLogger, StreamHandler
from os import path

db = SQLAlchemy()
login_manager = LoginManager()

def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)

def register_blueprints(app):
    for module_name in ('base', 'home'):
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)

def configure_database(app):

    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()

def configure_logs(app):
    # soft logging
    try:
        basicConfig(filename='error.log', level=DEBUG)
        logger = getLogger()
        logger.addHandler(StreamHandler())
    except:
        pass

def apply_themes(app):
    """
    Add support for themes.

    If DEFAULT_THEME is set then all calls to
      url_for('static', filename='')
      will modfify the url to include the theme name

    The theme parameter can be set directly in url_for as well:
      ex. url_for('static', filename='', theme='')

    If the file cannot be found in the /static/<theme>/ location then
      the url will not be modified and the file is expected to be
      in the default /static/ location
    """
    @app.context_processor
    def override_url_for():
        return dict(url_for=_generate_url_for_theme)

    def _generate_url_for_theme(endpoint, **values):
        if endpoint.endswith('static'):
            themename = values.get('theme', None) or \
                app.config.get('DEFAULT_THEME', None)
            if themename:
                theme_file = "{}/{}".format(themename, values.get('filename', ''))
                if path.isfile(path.join(app.static_folder, theme_file)):
                    values['filename'] = theme_file
        return url_for(endpoint, **values)

def create_app(config, selenium=False):
    app = Flask(__name__, static_folder='base/static')
    app.config.from_object(config)
    #if database_exists(app.config['SQLALCHEMY_DATABASE_URI']) == False:
    #    raise Exception("Database does not exist, check your DataBase path and ensure that you've started FTS")
    # UI configuration
    # UI version DO NOT modify it
    app.config['UIVERSION'] = '1.9.5'

    # number of milliseconds to query FTS for connected Users, health, a System status
    app.config['USERINTERVAL'] = '180000';
    app.config['SERVERHEALTHINTERVAL'] = '180000';
    app.config['SYSSTATUSINTERVAL'] = '600000';
    app.config['DATAPACKAGESIZELIMIT'] = '15360000';
    if selenium:
        app.config['LOGIN_DISABLED'] = True
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)
    configure_logs(app)
    apply_themes(app)
    return app
