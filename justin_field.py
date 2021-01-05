#created by justin field with help from the internet


import yaml

#Variable
company_name = 'WWT'
email_address = 'justin.field@wwt.com'
given_name = 'justin'
sur_name = 'field'
github_user = 'justinrfield'

justin_field_info = [{'company': company_name, 'email':email_address, 'first_name': given_name, 'last_name': sur_name, 'github_username': github_user}]


with open('justin_field.yml', 'w') as file:
  documents = yaml.dump(justin_field_info, file)
