# chris_hammond.py 6-15-2020
# created by Chris Hammond (ChrisHammond.com)
# https://github.com/jandiorio/study_group_screen
# Create a simple python script named <first_name>_<last_name>.py example: jeff_andiorio.py
#   - Creates a list of dictionaries with a single dictionary
#   - dictionary will have the following keys: ['first_name', 'last_name', 'company', 'email', 'github_username']
#   - dictionary will have your information as the values
#   - convert the list to a YAML string
#   - write the YAML string to a file

# import modules
import yaml # pip install pyyaml for installation

# create list with a dictionary 
mydict = [{
    'first_name': 'Chris',
    'last_name': 'Hammond',
    'company': 'WWT',
    'email': 'chris.hammond@wwt.com',
    'github_username': 'chrishammond'
}]

with open('chris_hammond.yaml','w') as output:
    yaml.dump(mydict,output)













































# what are you doing here?