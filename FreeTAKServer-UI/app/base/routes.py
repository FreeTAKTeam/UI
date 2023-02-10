# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from flask import jsonify, render_template, redirect, request, url_for
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user
)

from app import db, login_manager
from app.base import blueprint
from app.base.forms import LoginForm, CreateAccountForm
from app.base.models import User
from flask import current_app as app
from app.base.util import verify_pass

@blueprint.route('/')
def route_default():
    return redirect(url_for('base_blueprint.login'))

@blueprint.route('/error-<error>')
def route_errors(error):
    return render_template('errors/{}.html'.format(error))

## Login & Registration

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if 'login' in request.form:
        import requests
        # read form data
        username = request.form['username']
        password = request.form['password']

        # Locate user
        user = requests.get(f"{app.config['PROTOCOL']}://{app.config['IP']}:{app.config['PORT']}/AuthenticateUser", params={"username": username, "password": password}, headers={"Authorization": f"{app.config['APIKEY']}"})
        try:
            user = user.json()
        except:
            return render_template('login/login.html', msg='Wrong user or password', form=login_form)
        
        # Check the password
        if user:
            user = User(uid = user["uid"])
            db.session.add(user)
            db.session.commit()
            login_user(user)
            z = current_user
            url = url_for('base_blueprint.route_default')
            new_redr = redirect(url)
            return new_redr

        # Something (user or pass) is not ok
        return render_template( 'login/login.html', msg='Wrong user or password', form=login_form)
    z = current_user
    if not current_user.is_authenticated:
        return render_template( 'login/login.html',
                                form=login_form)
    return redirect(url_for('home_blueprint.index'))

@blueprint.route('/logout')
def logout():
    db.session.delete(current_user)
    db.session.commit()
    logout_user()

    return redirect(url_for('base_blueprint.login'))

@blueprint.route('/shutdown')
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server shutting down...'

## Errors

@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('errors/403.html'), 403

@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('errors/403.html'), 403

@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500
