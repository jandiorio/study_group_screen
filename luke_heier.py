myList = [
	{
		'first_name':'Luke',
		'last_name':'Heier',
		'company':'Jamf',
		'email':'luke.heier@jamf.com',
		'github_username':'heierlu'
	}
]

import yaml
with open(r'/Users/luke.heier/study_group_screen/luke_heier.yaml','w') as file:
	documents = yaml.dump(myList, file)