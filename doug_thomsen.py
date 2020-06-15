#doug_thomsen.py ver 1.2 (playing with VSCode)
#create by Doug Thomsen
#creates one list with one dictionary inside and prints to yaml file

#importing needed modules
import yaml

#creating list with one dictionary inside
listdoug = [
    {
        'first_name': 'Doug',
        'last_name': 'Thomsen',
        'company': 'WWT',
        'email': 'doug.thomsen@wwt.com',
        'github_username': 'dathomsen'
    }
        ]

with open('doug_thomsen.yaml', "w") as output:
    yaml.dump(listdoug, output)