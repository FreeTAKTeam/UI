#!/bin/bash

# Detect and navigate to the python user site packages
# Some systems use `python3` instead of `python` so this is not entirely portable
PYTHON_USER_SITE=$(python -m site --user-site)

python "${PYTHON_USER_SITE}/FreeTAKServer-UI/run.py"