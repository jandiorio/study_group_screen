#WWT DevNet pre-req to create file and show interest in joining group
#Create a YAML file containing basic "about me info"
##- Creates a **list** of dictionaries with a **single** dictionary
##- dictionary will have the following keys:  `['first_name', 'last_name', 'company', 'email', 'github_username']`
##- dictionary will have your information as the values
##- convert the list to a YAML string
##- write the YAML string to a file

import os
import yaml
print('====================')    

info_list = {}
info_list = {'first_name': 'Jeff', 'last_name': 'Orr', 'company': 'World Wide Technology', 'email': 'Jeff.Orr@wwt.com', 'github_username': 'jeffborr'}

PATH = os.getcwd() + '/jeff_orr.yaml'
print('File being written:', PATH)
print()

try:
    os.remove(PATH)
    print("Old File Removed!")
except OSError:
    print("No existing file")
    pass
print('====================')    

yaml_output = yaml.dump(info_list, explicit_start=True, sort_keys=False, default_flow_style=False)

print('YAML Output')
print(yaml_output)

file = open(PATH, "w")
file.write(yaml_output)
file.close()
