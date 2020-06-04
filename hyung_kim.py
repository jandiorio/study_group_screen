import yaml

myinfo = [{'first_name' : 'Hyung',
    'last_name' : 'Kim',
    'company' : 'WWT',
    'email' : 'hyung.kim@wwt.com',
    'github_username' : 'kimh66'
}]

with open('hyung_kim.yml','w') as file:
    yaml.dump(myinfo,file)

