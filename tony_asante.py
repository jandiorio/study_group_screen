#!/usr/bin/env python

import os
import yaml
import copy

#Using Native Python Dictionary

#whoami = {'first_name': 'Tony', 'last_name': 'Asante', 'company': 'WWT', 'email': 'tony.asante@wwt.com'}

#print(whoami)

#Using YAML
a_yaml_file = open("tony_asante.yaml")
parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)

print(parsed_yaml_file["company"])
