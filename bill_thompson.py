#!/usr/bin/python3

import yaml

#Create a dictionary of my information

myinfo = [

    {
        "company":  "WWT",
        "email": "bill.thompson@wwt.com",
        "first_name":  "Bill",
        "last_name":  "Thompson",
        "github_username": "wthomps413"
    }
]

#Convert the dictionary to YAML and output into file 

with open (r'bill_thompson.yaml', 'w') as file:
     info = yaml.dump(myinfo, file)
