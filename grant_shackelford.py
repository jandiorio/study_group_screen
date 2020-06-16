#1/usr/bin/env/python

import yaml

grant_shackelford = [{'first_name': 'Grant', 'last_name': 'Shackelford', 'company': 'WWT', 'email': 'grant.shackelford@wwt.com', 'github_username': 'IWriteBadCode'}]

with open('grant_shackelford.yaml', 'w') as f:

	data = yaml.dump(grant_shackelford, f)
	

