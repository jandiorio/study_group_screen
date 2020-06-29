import yaml

personal_info = [
    {
        'first_name': 'Chris',
        'last_name': 'Radford',
        'company': 'WWT',
        'email': 'chris.radford@wwt.com',
        'github_username': 'caradford86'
    }
]

with open('personal_info.yml', 'w') as output:
    yaml.dump(personal_info, output, default_flow_style=False)
