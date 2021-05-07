import yaml # allows for dump in yaml format

# Create a dictionary list, Note: [] makes it a hierarchical list
myList = [{'first_name':'Steve',
            'last_name':'Leapley',
            'company':'WWT',
            'email':'steve.leapley@wwt.com',
            'github_username':'leapleys'}]

file = open('steve.leapley.yaml', 'w')  # 'w' means create\open
file.write(yaml.dump(myList))
file.close() 