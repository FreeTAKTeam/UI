# FTS Web UI

FTS webUI allows administrators to easily manage the FTS server.
This component requires a working backend.
This video, based on a pre-production version,  provides an overview of most features described in the manual
https://www.youtube.com/watch?v=q4BpolzIDLw&ab_channel=%2aDA-B6%2a 
The WebUI is a completely separate application connecting to  the FTS backend. 
It uses an API to seamless query server functions. Depending on his deployment, may or may not be  seen from remote machines.


FTS, also offers a separate Command Line Interface (CLI). Follow this lik for his documentation https://freetakteam.github.io/FreeTAKServer-User-Docs/CLI/. 

Installation and configuration
This section provides an overview of the installation process. Refer to the online documentation for details. 

To install FTS and the UI type in a console
```
sudo python3 -m pip install FreeTAKServer[ui]
```
Setup your Configuration
your administrator will need to configure the following files
```
Config.py for the UI
MainConfig.py for FTS
```

###Start FTS
```nohup sudo python3 -m FreeTAKServer.controllers.services.FTS -DataPackageIP [YourIP] -AutoStart True nohup sudo python3 -m 
```

Start the WebUI
```nohup  sudo FLASK_APP=/usr/local/lib/python3.8/dist-packages/FreeTAKServer-UI/run.py python3 
```
## Dashboard Features

- SQLite,  
- Alembic (DB schema migrations)
- Modular design with **Blueprints**
- Session-Based authentication (via **flask_login**)
- Forms validation
 
- **MIT License**
 
#
## How to use it

`
