import yaml
myList = [
	{
	'first_name': 'swamy',
      	'last_name': 'goundar',
      	'company': 'Premera Bluecross',
      	'email': 'swamy.goundar@premera.com', 
      	'github_username': 'psgoundar'
	}

]
#print("print")
#print(myList[0])
print(yaml.dump(myList))

file = open("swamy.goundar.txt", "w")
yaml.dump(myList, file)
file.close()
