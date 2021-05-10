#!/usr/bin/env python3

import yaml

#create a list with a single dictionary
list = [{
    'first_name'      : 'Nathan',
    'last_name'       : 'Ritsch',
    'company'         : 'M Health Fairview',
    'email'           : 'nritsch@fairview.org',
    'github_username' : 'nritsch'
}]

#convert list to yaml string and write to file
f = open('nathan_ritsch.yaml', 'w')
f.write(yaml.dump(list))
f.close()

