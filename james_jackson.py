#!/usr/bin/python
import yaml

dict = [{'first_name': 'James', 'last_name': 'Jackson', 'company': 'The Boeing Company', 'email': 'james.w.jacksonjr@boeing.com', 'github_username': 'jwjacks' }]

f = open('myinfo.yaml', 'w+')
yaml.dump(dict, f)
