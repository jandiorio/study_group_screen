#created by drew milles super noob

import yaml

#values
first_name = 'drew'
last_name = 'milles'
company = 'WWT'
company_email = 'drew.milles@wwt.com'
github_username = 'millesd'

#dictionary
mydictionary = [
    {
        'first_name':first_name,
        'last_name':last_name,
        'company':company,
        'company_email':company_email,
        'github_username':github_username,

    }
]

#write to yaml
with open('drew_milles.yaml', 'w') as my_file:
    output_file = yaml.dump(mydictionary, my_file)