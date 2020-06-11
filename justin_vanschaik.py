#!/usr/bin/python2.7

import yaml

dict_file = dict([('first_name', 'Justin'), ('last_name', 'vanSchaik'), ('company', 'WWT'), ('email', 'justin.vanschaik@wwt.com'), ('github_username', 'jvanschaik')])

with open ('justin_vanschaik.yaml', 'w') as file:
     documents = yaml.dump(dict_file, file)
