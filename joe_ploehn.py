#!/usr/bin/env python
"""
Program Name: joe_ploehn.py

Program Description: Create a yaml file with certain personal information
Program Requirements:
    pyyaml module

"""
import yaml

company = 'WWT'
email = 'joe.ploehn@wwt.com'
first_name = 'Joe'
last_name = 'Ploehn'
github_username = 'metalaxe64'
filename = 'joe_ploehn.yaml'

data = [{'company': company,'email': email, 'first_name': first_name, 'github_username': github_username, 'last_name': last_name }]

with open(filename, 'w') as file:
    yaml.dump(data, file)
