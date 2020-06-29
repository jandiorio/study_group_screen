import yaml

me = [{'first_name':'Jeff',
        'last_name':'Mercier', 
        'company':'WWT', 
        'email':'jeff.mercier@wwt.com', 
        'github_username':'jeffmercier'}]

me_yaml = yaml.safe_dump(me)

print(me_yaml)

with open('jeff_mercier.yml', 'w') as file:
    file.write(me_yaml)
