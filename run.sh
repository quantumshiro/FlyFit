#!/bin/bash

source ./venv/bin/activate
python main.py
sleep 2
python tensor.py
sleep 2
python sabun.py
sleep 2
python plot3.py
deactivate
