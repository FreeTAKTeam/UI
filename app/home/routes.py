
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

@blueprint.route('/index')
@login_required
def index():
    
    if not current_user.is_authenticated:
       return redirect(url_for('base_blueprint.login'))

    return render_template('index.html')



@blueprint.route('/mission')
@login_required
def missionApi():
   # response = requests.get('https://jsonplaceholder.typicode.com/posts')
    response = requests.get('http://localhost:3000/dataPackage')

    #headers = {'userAuthorizationname': 'Bearer a@v{5]MQU><waQ;Z'}

    #response = requests.get('http://204.48.30.216:19023/DataPackageTable', headers)
    #print('test..ZZ' + response)

    #return render_template('mission.html')    

    if response.status_code != 200:
        # This means something went wrong.
        print('{} {}'.format(response.status_code))
    
    #package_data_list = response.json()

    #package_data_list1 = response.json()
    

    #return render_template('mission.html', package_data_list = package_data_list,  package_data_list1 = package_data_list1 )
    return render_template('mission.html')


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
