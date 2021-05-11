import yaml

readmeList = [ 
    {
        'first_name': 'giovanni', 
        'last_name': 'delarosa', 
        'company': 'wwt', 
        'email': 'giovanni.delarosa@wwt.com', 
        'github_username': 'giodelarosa'
    }
]

#print (readmeList)

print (yaml.dump(readmeList))

with open(r'/Users/giovannidelarosa/study_group_screen/yamlFile.yaml', 'w') as file:
        documents = yaml.dump(readmeList, file)