import yaml

Mikes_info = dict(
  company='WWT',
  email= 'michael.witte@wwt.com',
  first_name= 'Michael',
  github_username= 'miwitte',
  last_name= 'Witte'
)
with open(r'C:\development\Jeffs challenge\Mikes_info.yaml', 'w') as file:
    documents = yaml.dump(Mikes_info, file)