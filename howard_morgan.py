import yaml

dict = {'first_name': 'howard', 'last_name': 'morgan', 'company': 'WWT', 'email': 'howard.morgan@wwt.com', 'github_username': 'homorgan'}
 
with open(r'howard_morgan.yaml', 'w') as file:
    yaml.dump(dict, file)
