#!/usr/bin/python

# Python program to convert a list of dictionaries to YAML 
# and write output to a file.
#
# Requirements:
#   pip install pyyaml
#
# Usage:
#   python lenny_ilyashov.py
#
# Sample YAML output:
#   - company: WWT
#     email: jeff.andiorio@wwt.com
#     first_name: Jeff
#     github_username: jandiorio
#     last_name: Andiorio
#

import yaml

# create list of dictionaries with a single dictionary
lenny_ilyashov_list = [
  {
    'first_name':"Lenny",
    'last_name':"Ilyashov",
    'company':"WWT",
    'email':"lenny.ilyashov@wwt.com",
    'github_username':"lennyi"
  }
]
#print(lenny_ilyashov_list)

# convert list to a YAML string
lenny_ilyashov_yaml=yaml.dump(lenny_ilyashov_list)
print(lenny_ilyashov_yaml)

# write the YAML string to file
lenny_ilyashov_file = open("lenny_ilyashov.yaml", "w")
yaml.dump(lenny_ilyashov_list, lenny_ilyashov_file)
lenny_ilyashov_file.close()

