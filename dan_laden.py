
import yaml

list = [{
    "company": "WWT",
    "email": "daniel.ladem@wwt.com",
    "first_name": "Dan",
    "github_username": "danielwwt",
    "last_name": "Laden"
}]

with open(r'dan_laden.yaml', 'w') as file:
    documents = yaml.dump(list, file)