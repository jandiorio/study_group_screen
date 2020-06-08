import yaml

dict_file = [
    {
        "first_name": "Rob",
        "last_name": "Rummel",
        "company": "WWT",
        "email": "rob.rummel@wwt.com",
        "github_username": "robrummel",
    }
]

with open("/Users/rummelr/Desktop/Python/rob.rummel.yaml","w") as file:
	documents = yaml.dump(dict_file, file)
	
