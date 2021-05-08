import yaml


myList = [
	{
	'first_name': "Jason",
	'last_name': "Kusner",
    'company': "Cardinal Health",
    'email': "jkusner@gmail.com",
    'github_username': "nojunkfree"
	}
]

yamlstring=yaml.dump(myList)

f = open("jason.yaml", "w")
f.write(yamlstring)
f.close()

