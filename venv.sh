#!/bin/bash

python3 -m venv ${1}
python3 -m pip install --upgrade pip
pip install ipykernel
python3 -m ipykernel install --user --name=${1}
