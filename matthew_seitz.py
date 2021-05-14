import yaml
dict = {'company': 'WWT','email': 'matthew.seitz@wwt.com','first_name': 'Matthew','github_username': 'mseitz83','last_name': 'Seitz'}

with open('matthew_seitz.yaml', 'w') as f:
    yaml_file = yaml.dump(dict)
    f.write(str(yaml_file))
    f.close
