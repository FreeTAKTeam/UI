
# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from app.home import blueprint
from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app import login_manager
from jinja2 import TemplateNotFound
import requests
from flask import current_app as app
from app.base.forms import UpdateAccountForm
from app.base.models import User
from app import db

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(uid=user_id).first()

@blueprint.route('/index')
@login_required
def index():
    
    if not current_user.is_authenticated:
       return redirect(url_for('base_blueprint.login'))

    return render_template('index.html', segment='index',
    websocketkey=app.config['WEBSOCKETKEY'], apikey=app.config['APIKEY'], port=app.config['PORT'], protocol=app.config['PROTOCOL'], ip=app.config['IP'],
    userinterval=app.config['USERINTERVAL'],serverhealthinterval=app.config['SERVERHEALTHINTERVAL'], sysstatusinterval=app.config['SYSSTATUSINTERVAL']
    )


@blueprint.route('/mission')
@login_required
def missionApi():
    
    headers = {'Authorization': app.config['APIKEY']}

    try:
        json_data = requests.get(f"{app.config['PROTOCOL']}://{app.config['IP']}:{app.config['PORT']}/DataPackageTable", headers= headers).json()
    except Exception as e:
        print(e)
        json_data = {'json_list': []}
    
    try:
        mission_json_data = requests.get(f"{app.config['PROTOCOL']}://{app.config['IP']}:{app.config['PORT']}/MissionTable", headers= headers).json()
    except Exception as e:
        print(e)
        mission_json_data = {'data': []}

    try:
        excheck_json_data = requests.get(f"{app.config['PROTOCOL']}://{app.config['IP']}:{app.config['PORT']}/ExCheckTable", headers= headers).json()
    except Exception as e:
        print(e)
        excheck_json_data = {'data': []}

    try:
        outgoing_federation_json_data = requests.get(f"{app.config['PROTOCOL']}://{app.config['IP']}:{app.config['PORT']}/FederationTable", headers= headers).json()
    except Exception as e:
        print(e)
        outgoing_federation_json_data = {'federations': []}
   
    return render_template('mission.html', json_data = json_data['json_list'], 
    mission_json_data = mission_json_data['data'],
    excheck_json_data = excheck_json_data['data'][0]['contents'],
    outgoing_federation_json_data = outgoing_federation_json_data['federations'],
    segment = "mission",
    websocketkey=app.config['WEBSOCKETKEY'], apikey=app.config['APIKEY'], port=app.config['PORT'], protocol=app.config['PROTOCOL'], ip=app.config['IP'],
    datapackagesizelimit=app.config['DATAPACKAGESIZELIMIT']
    
     )





@blueprint.route('/connect')
@login_required
def connectApi():
    headers = {'Authorization': app.config['APIKEY']}
    json_data = requests.get(f"{app.config['PROTOCOL']}://{app.config['IP']}:{app.config['PORT']}/ManageEmergency/getEmergency", headers= headers)
    json_data = json_data.json()
    
    return render_template('connect.html', json_data = json_data['json_list'], segment="connect",
    websocketkey=app.config['WEBSOCKETKEY'], apikey=app.config['APIKEY'], port=app.config['PORT'], protocol=app.config['PROTOCOL'], ip=app.config['IP'])     


@blueprint.route('/configure')
@login_required
def configureApi():
    headers = {'Authorization': app.config['APIKEY']}
    outgoing_federation_json_data = requests.get(f"{app.config['PROTOCOL']}://{app.config['IP']}:{app.config['PORT']}/FederationTable", headers= headers).json()

    return render_template('configure.html', segment="configure", 
    outgoing_federation_json_data = outgoing_federation_json_data['federations'],
    websocketkey=app.config['WEBSOCKETKEY'], apikey=app.config['APIKEY'], port=app.config['PORT'], protocol=app.config['PROTOCOL'], ip=app.config['IP'])

@blueprint.route('/users')
@login_required
def usersApi():
    return render_template('users.html', segment="users", 
    websocketkey=app.config['WEBSOCKETKEY'], apikey=app.config['APIKEY'], port=app.config['PORT'], protocol=app.config['PROTOCOL'], ip=app.config['IP'])     
      
@blueprint.route('/about')
@login_required
def aboutApi():
    return render_template('about.html', segment="about", uiversion=app.config['UIVERSION'],
    websocketkey=app.config['WEBSOCKETKEY'], apikey=app.config['APIKEY'], port=app.config['PORT'], protocol=app.config['PROTOCOL'], ip=app.config['IP'])     

@blueprint.route('/webmap')
@login_required
def webmapApi():
    return render_template('webmap.html', segment="webmap", uiversion=app.config['UIVERSION'],
    websocketkey=app.config['WEBSOCKETKEY'], apikey=app.config['APIKEY'],
    ip=app.config['IP'], protocol=app.config['PROTOCOL'], port=app.config['PORT'],
    webmapip=app.config['WEBMAPIP'], webmapport=app.config['WEBMAPPORT'], webmapprotocol=app.config['WEBMAPPROTOCOL'])

@blueprint.route('/page-user', methods=['GET', 'POST'])
@login_required
def page_user():
    import copy
    update_account_form = UpdateAccountForm(request.form)
    y = request.form
    if "update" in request.form:
        password = request.form['password']
        token = request.form['token']
        group = request.form['group']
        user = User.query.filter_by(uid=current_user.uid).first()
        user.token = token
        user.group = group
        user.password = password
        db.session.add(user)
        db.session.commit()
        return render_template('page-user.html', form=update_account_form)

    else:
        uid = copy.copy(current_user.uid)
        return render_template('page-user.html', form=update_account_form, ip=app.config["IP"], port=app.config["PORT"], websocketkey=app.config['WEBSOCKETKEY'], apikey=app.config['APIKEY'], user_id=uid)

@blueprint.route('/mission/<id>/qr')
def qr(id):
    qr_link = 'http://' + app.config['IP'] + ':' + app.config['PORT'] + '/GenerateQR'+ '?datapackage_id=' + id
    return render_template('qr.html', qr_link=qr_link)

@blueprint.route('/<template>')
def route_template(template):

    if not current_user.is_authenticated:
        return redirect(url_for('base_blueprint.login'))

    try:

        return render_template(template + '.html')

    except TemplateNotFound:
        return render_template('page-404.html'), 404
    
    except:
        return render_template('page-500.html'), 500


