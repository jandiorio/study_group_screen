#DevNet Study Group Tryout

import yaml

contact = [{'first_name': 'Craig'}, {'last_name': 'Wright'}, {'company': 'WWT'}, {'email': 'craig.wright@wwt.com'}, {'github_username': 'cwright613'}]

with open('contact.yaml', 'w') as f:
    data = yaml.dump(contact, f)


