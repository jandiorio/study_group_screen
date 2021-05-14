#!/usr/bin/env python3

# Import the safe_dump method from the pyyaml module
from yaml import safe_dump

# Specify the name for the output file
FILE_NAME = 'chris_fendya.yml'

# Create a list which contains one dictionary
about_me = [
    {
        'first_name': 'Chris',
        'last_name': 'Fendya',
        'company': 'Cohesity',
        'email': 'chris.fendya@cohesity.com',
        'github_username': 'chrisfendya',
    }
]

# Convert the dictionary to a YAML string
about_me_yaml = safe_dump(about_me)

with open(
    file=FILE_NAME,
    mode='wt',
    encoding='utf-8'
) as file:
    file.write(about_me_yaml)