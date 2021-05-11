import yaml

data = [{
"company": "jamf",
"first_name": "Piotr",
"last_name": "Becker",
"email": "piotr.becker@jamf.com",
"github_username": "piotrbecker"
}]

print(yaml.dump(data))

with open('piotr_becker.yaml', 'w') as file:
	yaml.dump(data, file, default_flow_style=False)