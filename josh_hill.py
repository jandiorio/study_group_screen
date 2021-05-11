#!/usr/bin/env python3
"""
05/11/2021
"""
import yaml

list = [{'first_name': 'josh', 'last_name': 'hill', 'company': 'U.S. Bank', 'email': 'josh.hill@usbank.com', 'github_username': 'i3uiw'}]
list_str = yaml.dump(list)
with open('list.yaml', 'w') as file:
    yaml.dump(list, file)
