#!/bin/bash

cd /home/mcpa/api/
python3 api_manager.py -v problems load /home/mcpa/example_problems graders/ ../problem_static/
python3 api_manager.py autogen build 100
devploy
