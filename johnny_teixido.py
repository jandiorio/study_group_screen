#!/usr/bin/env python3

import yaml

johnteixido = [{'first_name': 'Johnny', 'last_name': 'Teixido', 'company': 'Truist', 'email': 'john.teixido@truist.com', 'github_username': 'JT252' }]

with open('johnnyteixido.yaml', 'w') as jt:

    data = yaml.dump(johnteixido, jt)
