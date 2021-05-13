# - company: WWT
#   email: jeff.andiorio@wwt.com
#   first_name: Jeff
#   github_username: jandiorio
#   last_name: Andiorio

# import yaml

# users = [{'name': 'John Doe', 'occupation': 'gardener'},
#          {'name': 'Lucy Black', 'occupation': 'teacher'}]

# with open('users.yaml', 'w') as f:
    
#     data = yaml.dump(users, f)

import yaml

about_me = [{ 
    'Company': 'Premera',
    'email': 'wagsbjj@hotmail.com',
    'first_name': 'michelle',
    'github_username': 'wagsbjj',
    'last_name': 'wagner'}]

# The dump() method serializes a Python object into a YAML stream
# print(yaml.dump(about_me)) 

# The following example writes Python data into a YAML file.
with open('about_me.yaml', 'w') as f:
    data = yaml.dump(about_me, f)