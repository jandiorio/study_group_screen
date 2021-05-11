#
#
#
#

import yaml

dict_file = [{
    "company": "US Bank",
    "email": "matthew.leis@sbank.com",
    "first_name": "Matt",
    "github_username": "mleis42",
    "last_name": "Leis"
}]

with open(r'matt_leis.yaml', 'w') as file:
    documents = yaml.dump(dict_file, file)


