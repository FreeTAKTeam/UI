# # -*- encoding: utf-8 -*-
# """
# License: Commercial
# Copyright (c) 2019 - present AppSeed.us
# """

# from flask_migrate import Migrate
# from os import environ
# from sys import exit

# from config import config_dict
# from app import create_app, db

# get_config_mode = environ.get('APPSEED_CONFIG_MODE', 'Debug')

# try:
#     config_mode = config_dict[get_config_mode.capitalize()]
# except KeyError:
#     exit('Error: Invalid APPSEED_CONFIG_MODE environment variable entry.')

# app = create_app(config_mode) 
# Migrate(app, db)

# if __name__ == "__main__":
#     app.run()


# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_migrate import Migrate
from os import environ
from sys import exit
from decouple import config

from config import config_dict
from app import create_app, db

from argparse import ArgumentParser

# WARNING: Don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True)

# The configuration
get_config_mode = 'Debug' if DEBUG else 'Production'

try:
    
    # Load the configuration using the default values 
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

app = create_app( app_config ) 

# Get args if present and assign them
"""if __name__ == '__main__':
    # Initialize the arg parser
    parser = ArgumentParser(
        description=""
    )
    parser.add_argument(
        '-i', '--ip_address', type=str, help='ip address of the target host'
        , required=False)
    parser.add_argument(
        '-ap', '--api_port', type=int, help='Port of the target host'
        , required=False)
    parser.add_argument(
        '-ac', '--api_protocol', type=str, help='Protocol of the target host'
        , required=False)
    parser.add_argument(
        '-k', '--key', type=str, help='Web Socket key for the UI'
        , required=False)
    parser.add_argument(
        '-p', '--port', type=int, help='Port for the Web UI HTTP'
        , required=False)
    parser.add_argument(
        '-c', '--protocol', type=str, help='Protocol serving the Web UI HTTP'
        , required=False)
    parser.add_argument(
        '-wi', '--webmap_ip', type=str, help='ip address of the webmap host'
        , required=False)
    parser.add_argument(
        '-wc', '--webmap_protocol', type=str, help='protocol of the webmap host'
        , required=False)
    parser.add_argument(
        '-wp', '--webmap_port', type=int, help='port of the webmap host'
    parser.add_argument(
        '-d','--debug', default=False, dest='debug',action='store_true'
        ,help='Enable Debug mode')

    # Parse the arguments
    arguments = parser.parse_args()

    # Finally print the passed string
    #print("args are:")
    #print(arguments)
    # If arg is passed, set it in the config structure
    if arguments.ip_address:
        print("IP Address override: " + str(arguments.ip_address))
        app.config['IP'] = arguments.ip_address
    if arguments.api_port:
        print("API Port override: " + str(arguments.api_port))
        app.config['PORT'] = arguments.api_port
    if arguments.api_protocol:
        print("API Protocol override: " + str(arguments.api_protocol))
        app.config['PROTOCOL'] = arguments.api_protocol
    if arguments.webmap_ip:
        print("Web Map IP override: " + str(arguments.webmap_ip))
        app.config['WEBMAPIP'] = arguments.webmap_ip
    if arguments.webmap_protocol:
        print("Web Map Protocol override: " + str(arguments.webmap_protocol))
        app.config['WEBMAPPROTOCOL'] = arguments.webmap_protocol
    if arguments.webmap_port:
        print("Web Map Port override: " + str(arguments.webmap_port))
        app.config['WEBMAPPORT'] = arguments.webmap_port
    if arguments.key:
        print("Web Socket Key override: " + str(arguments.key))
        app.config['WEBSOCKETKEY'] = arguments.key
    if arguments.port:
        print("Web Port override: " + str(arguments.port))
        # Have to use app_config rather than app.config
        app_config.APPPort = arguments.port
    if arguments.debug:
        print("Debug mode enabled")
        DEBUG= True
    else:
        DEBUG= False
    app.run()"""

Migrate(app, db)

if __name__ == "__main__":
    import eventlet
    from eventlet import wsgi, wrap_ssl
    wsgi.server(sock = eventlet.listen((app_config.APPIP, app_config.APPPort)), site=app)
    #app.run(debug=True)
    # app.run()
