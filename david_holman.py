#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml

dict_file = [{'company' : ['WWT']}, {'first_name' : ['David']}, {'last_name' : ['Holman']}, {'github_username' : ['dholman_wwt']}, {'email' : ['david.holman@wwt.com']}]

with open('david_holman.yaml', 'w') as file:
    documents = yaml.dump(dict_file, file)
