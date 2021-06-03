import yaml

#Creates a list of dictionary pairs
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

#prints the dic in yaml format
print (yaml.dump(readmeList))


#Creates a file call yamlFile in the studygroup directory 
#by openning it and writting the list call readmeList 
#the list gets written in yaml format using the yaml.dump

with open(r'/Users/giovannidelarosa/study_group_screen/yamlFile.yaml', 'w') as file:
        documents = yaml.dump(readmeList, file)