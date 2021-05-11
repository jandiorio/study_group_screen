import yaml

assignment = [{'first_name': 'Jim',
               'last_name': 'Mathers',
               'company': 'SAS',
               'email': 'jim.mathers@sas.com',
               'github_username': 'jimmathers'}]

with open('assignment.yaml', 'w') as f:
    data = yaml.dump(assignment, f)