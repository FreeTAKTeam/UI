
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

@blueprint.route('/index')
@login_required
def index():
    
    if not current_user.is_authenticated:
       return redirect(url_for('base_blueprint.login'))

    return render_template('index.html', segment='index',
    websocketkey=app.config['WEBSOCKETKEY'], apikey=app.config['APIKEY'], port=app.config['PORT'], ip=app.config['IP'],
    userinterval=app.config['USERINTERVAL'],serverhealthinterval=app.config['SERVERHEALTHINTERVAL'], sysstatusinterval=app.config['SYSSTATUSINTERVAL']
    )


@blueprint.route('/mission')
@login_required
def missionApi():
    
    headers = {'Authorization': app.config['APIKEY']}

    json_data = requests.get('http://' + app.config['IP'] + ':' + app.config['PORT'] + '/DataPackageTable', headers= headers).json()
    
    mission_json_data = requests.get('http://' + app.config['IP'] + ':' + app.config['PORT'] + '/MissionTable', headers= headers).json()

    excheck_json_data = requests.get('http://' + app.config['IP'] + ':' + app.config['PORT'] + '/ExCheckTable', headers= headers).json()

    outgoing_federation_json_data = requests.get('http://' + app.config['IP'] + ':' + app.config['PORT'] + '/FederationTable', headers= headers).json()
    
   
    return render_template('mission.html', json_data = json_data['json_list'], 
    mission_json_data = mission_json_data['data'],
    excheck_json_data = excheck_json_data['ExCheck']['Templates'],
    outgoing_federation_json_data = outgoing_federation_json_data['federations'],
    segment = "mission",
    websocketkey=app.config['WEBSOCKETKEY'], apikey=app.config['APIKEY'], port=app.config['PORT'], ip=app.config['IP']
    
     )





@blueprint.route('/connect')
@login_required
def connectApi():
    headers = {'Authorization': app.config['APIKEY']}
    json_data = requests.get('http://' + app.config['IP'] + ':' + app.config['PORT'] + '/ManageEmergency/getEmergency', headers= headers).json()
    
    return render_template('connect.html', json_data = json_data['json_list'], segment="connect",
    websocketkey=app.config['WEBSOCKETKEY'], apikey=app.config['APIKEY'], port=app.config['PORT'], ip=app.config['IP'])     


@blueprint.route('/configure')
@login_required
def configureApi():
    headers = {'Authorization': app.config['APIKEY']}
    outgoing_federation_json_data = requests.get('http://' + app.config['IP'] + ':' + app.config['PORT'] + '/FederationTable', headers= headers).json()

    return render_template('configure.html', segment="configure", 
    outgoing_federation_json_data = outgoing_federation_json_data['federations'],
    websocketkey=app.config['WEBSOCKETKEY'], apikey=app.config['APIKEY'], port=app.config['PORT'], ip=app.config['IP'])

@blueprint.route('/users')
@login_required
def usersApi():
    return render_template('users.html', segment="users", 
    websocketkey=app.config['WEBSOCKETKEY'], apikey=app.config['APIKEY'], port=app.config['PORT'], ip=app.config['IP'])     
      
@blueprint.route('/about')
@login_required
def aboutApi():
    return render_template('about.html', segment="about", uiversion=app.config['UIVERSION'],
    websocketkey=app.config['WEBSOCKETKEY'], apikey=app.config['APIKEY'], port=app.config['PORT'], ip=app.config['IP'])     

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


