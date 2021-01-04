#!/usr/bin/env python
"""
eric_fairfield.py
written by Eric Fairfield (ericfairfield)
Copyright (C) 2020 World Wide Technology
All Rights Reserved

This application will take the variables and place them into a dictionary. The dictionary will dump the contents into a yaml file.
"""

import yaml

var_company = 'WWT'
var_email = 'eric.fairfield@wwt.com'
var_firstname = 'Eric'
var_lastname = 'Fairfield'
var_github_username = 'ericfairfield'

user_info = {'company': var_company, 'email':var_email,'first_name':var_firstname,'last_name': var_lastname,'github_username': var_github_username }

with open(r'./info.yaml', 'w') as file:
    info_file = yaml.dump(user_info, file)
    