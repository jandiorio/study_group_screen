#!/usr/bin/env python

import yaml

# Define Variables
em_first = 'Eunice'
em_last = 'Muthuswami'
em_company = 'WWT'
em_email = 'eunice.muthuswami@wwt.com'
em_username = 'eunidc'

# My information in dictionary format
myinfo = [
	{
		'company':em_company,
		'email':em_email,
		'first_name':em_first,
        	'github_username':em_username,
		'last_name':em_last,
	}
]

# Write to file in yaml format
with open('./eunice_muthuswami.yaml', 'w') as my_file:
    output_file = yaml.dump(myinfo, my_file)
