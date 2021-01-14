import yaml

file = open("jason_hartsock.yml", "w")

key_value = [{'company' : 'Boeing', 'email' : 'jason.hartsock@boeing.com', 'first_name':'Jason', 'last_name':'Hartsock', 'github_username':'captjwh'}]

contents = yaml.dump(key_value)
#print(contents)
file.write(contents)
file.close()
