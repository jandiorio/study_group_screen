#!/usr/bin/env python

#@Author: Carl Dubois
#@Email: carl.dubois@wwt.com
#@Description: Jeff A's cool devnet test

import json, ast
import yaml 

with open('carl.json') as json_file: 
    data = json.load(json_file)
    data = ast.literal_eval(json.dumps(data)) # remove pesky unicode
    outfile = [data]

with open(r'./carl.yaml', "w+") as file:
    doc = yaml.dump(outfile, file)

print 'First:', str(data['first_name'])
print 'Last:', str(data['last_name'])
print 'Company:', str(data['company'])
print 'Email:', str(data['email'])
print 'Git:', str(data['github_username'])