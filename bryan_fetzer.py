#!/usr/bin/env python3

import yaml

input_dict = [{'company': 'WWT', 'email': 'bryan.fetzer@wwt.com', 'first_name': 'Bryan', 'github_username': 'haljordan2814', 'last_name': 'Fetzer'}]

with open('bryan_fetzer.yaml', 'w') as f:

    data = yaml.dump(input_dict, f)