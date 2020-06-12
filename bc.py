#!/usr/bin/env python
"""
bruce.clounie.py

    Copyright (c) 2020 World Wide Technology, Inc.
    All rights reserved.

    author: bruce.clounie@wwt.com
    written:  9 June 2020
    description:

        The code outputs user information into a yaml file

    changes:

    notes:

     
    requirements:
       
       pyyaml module

    examples:
       

"""
import yaml

# Define Variables

info_company = 'wwt'
info_email = 'bruce.clounie@wwt.com'
info_first_name = 'Bruce'
info_last_name = 'Clounie'
info_github_username = 'bclounie57'

#Define String of Dictionary(s) 

info = [{'company':info_company,'email':info_email, 'first_name':info_first_name, 'github_username': info_github_username, 'last_name':info_last_name }]

#Write yaml file as single list of key:value pairs

with open(r'./info_file.yaml', 'w') as file:
    documents = yaml.dump(info, file)