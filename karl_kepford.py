import yaml
# data info ie name, company, email ,etc
myInfo = [ {'first_name': "Karl", 'last_name' : "Kepford" ,'company': "BassPro Shops", 'email': "klkepford@basspro.com", 'github_username': "kkepford"}]
#print to validate info 
print(yaml.dump(myInfo))

#define for write to file
yamlinfo=yaml.dump(myInfo)
#open file name and write (write)
file = open("karl.yaml", "w")
file.write(yamlinfo)
#close file
file.close()
