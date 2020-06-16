import yaml

dict_file = [{ "company" : "WWT", "email" : "tim@russellweb.eu", "first_name" : "Tim", "last_name" : "Russell", "github_username" : "timr1972" } ]

with open(r'tim_russell.yaml', 'w') as file:
	documents = yaml.dump(dict_file, file)
