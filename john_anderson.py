#!/usr/bin/env python3

# YAML library needed to output in desired format
import yaml

# Create the data
john_list = []
john_list.append( {
	'first_name': 'John',
	'last_name': 'Anderson',
	'company': 'WWT',
	'email': 'john.anderson@wwt.com',
	'github_username': 'John'
} )

# Format in YAML
john_yaml = yaml.dump(john_list)

# Write to file
f = open('john_anderson.yml', 'w')
f.write(john_yaml)
f.close
