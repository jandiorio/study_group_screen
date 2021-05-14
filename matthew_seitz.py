import yaml
dict = {'company': 'WWT','email': 'matthew.seitz@wwt.com','first_name': 'Matthew','github_username': 'mseitz83','last_name': 'Seitz'}

f = open('matthew_seitz.yaml', 'w')
f.write(yaml.dump(dict))
f.close()
