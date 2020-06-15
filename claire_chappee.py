import yaml

#my values for the dict
claires_company = 'WWT'
claires_email = 'claire.chappee@wwt.com'
claires_first_name = 'Claire'
claires_last_name = 'Chappee'
claires_github_username = 'cchappee'

#
info = [{'first_name':claires_first_name,'last_name':claires_last_name,'company':claires_company,'email':claires_email,'github_username': claires_github_username }]

with open(r'./claires_info.yaml', 'w') as file:
    documents = yaml.dump(info, file)