#!/bin/bash

# Update this to not be hard-coded
cd /home/freetak/.local/lib/python3.11/site-packages/FreeTAKServer-UI/ || (echo "Something has gone very wrong" && exit)

# OBE as this is handled in the dockerfile
# If config.py exists
#if test -f config.py; then
  # Then we need to move it to a "backup"
  # this way we can always give the user a new one if they delete theirs
#  mv config.py config.bak
#fi

# Check if there is *NOT* a config.py in the shared volume
if [[ ! -f "/home/freetak/data/config.py" ]]
  then
    # If there isn't, then we need to give one to the user
    cp config.bak /home/freetak/data/config.py
fi

# If the symlink has not been created yet, then we will do that
if [[ ! -f "config.py" ]]
  then
    ln -s /home/freetak/data/config.py config.py
fi

# Now we can start the server
python run.py