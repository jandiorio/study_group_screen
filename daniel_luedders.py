import yaml

devInfo = [
   {
	'first_name':'Daniel',
	'last_name':'Luedders',
	'github_username':'luedderd',
	'company':'World Wide Technology',
	'email':'daniel.luedders@wwt.com'
   }
]

with open('DeveloperInfo.yaml', 'w') as yaml_file:
    output_file = yaml.dump(devInfo, yaml_file)
