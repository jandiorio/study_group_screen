import yaml

data = {'Company': 'WWT',
         'email': 'kevin.chen@wwt.com',
         'first_name': 'Kevin',
         'github_username': 'kevin-chen1234567',
         'last_name': 'Chen'
         }

yaml.dump(data)

print(yaml.dump(data))