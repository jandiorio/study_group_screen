import yaml


wwtinfo = {
    'first_name': 'Chad',
    'last_name': 'Drier',
    'company': 'Jamf',
    'email': 'chad.drier@jamf.com',
    'github_username': 'chaddrier'
}
print(wwtinfo)

yaml.dump(wwtinfo, explicit_start=True, default_flow_style=False)
