import yaml

dict_file = [{'first_name': 'thanh', 'last_name': 'chau', 'company': 'wwt', 'email': 'thanh.chau@wwt.com', 'github_username':'meggathanh'}]
# print(dict_file)

with open(r'./thanh.yaml', 'w') as file:
	documents = yaml.dump(dict_file, file)
