#!/usr/bin/env python3

# Import Module Dependencies
import yaml


# Create Dictionary w/List of Variables
github_info = dict(first_name='Rick', last_name='Hydorn', company='Premera', email='rick.hydorn@premera.com', github_username='rickhydorn')

# Print dictionary info from 'github_info' variable in YAML format
print (yaml.dump(github_info, sort_keys=False))

# Write dictionary info from 'github_info' variable to a file in YAML format
with open('github-info.yml', 'w') as outputfile:
  yaml.dump(github_info, outputfile, sort_keys=False)
