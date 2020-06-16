import yaml

person = {
    'first_name' : 'Sohail', 'last_name' : 'Zafar', 'company' : 'WWT', 'email' : 'Sohail_Zafar@wwt.com', 'github_userid' : 'szafars'
}

for x, y in person.items():
    print(x+': ' + y)

with open('data.yml' , 'w') as outfile:
    yaml.dump(person, outfile, default_flow_style=False)