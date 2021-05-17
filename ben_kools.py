import yaml

dict_file = [{'first_name':'Ben', 'last_name':'Kools', 'company':'WWT', 'email':'ben.kools@wwt.com', 'github_username':'koolsb'}]

with open(r'ben_kools.yaml', 'w') as file:
	documents = yaml.dump(dict_file, file)