import yaml
my_info = [{
'first_name': 'John',
'company': 'WWT',
'last_name': 'Rauma',
'email': 'john.rauma@wwt.com',
'github_username': 'jrauma'
}]
with open('john_rauma.yaml', 'w') as f:
    f.write(yaml.safe_dump(my_info))