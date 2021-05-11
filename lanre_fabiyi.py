data = [
   {'name':'first_name', 'value': 'lanre'},
   {'name':'last_name' , 'value': 'fabiyi'},
   {'name':'company', 'value': 'WWT'},
   {'name':'email' , 'value' : 'lanre.fabiyi@literaysng.com'},
   {'name':'github_username' , 'value' : 'larrybiyi'}
] 

new_dict = {x['name']: x['value'] for x in data}

print(new_dict)



import yaml

print(yaml.dump(new_dict))


with open(r'/home/ansible/study_group_screen/store_file.yaml', 'w') as file:
    documents = yaml.dump(new_dict, file)


with open(r'/home/ansible/study_group_screen/store_file.yaml') as file:
     doc = yaml.load(file, Loader=yaml.FullLoader)

     sort_file = yaml.dump(doc, sort_keys=True)
     print(sort_file)
