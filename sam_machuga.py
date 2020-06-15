#!/usr/bin/env python3

import yaml

def main():

	contactInfo = [{'company': 'WWT', 'email': 'sam.machuga@wwt.com',
					'first_name': 'Sam', 'last_name': 'Machuga', 
					'github_username': 'machoog546'}]

	with open('sam_machuga.yaml', 'w') as output:
	
		yaml.dump(contactInfo, output)



main()