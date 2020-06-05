import yaml

dict_file = [{'first_name' : 'Damon', 'last_name' : 'Watson', 'company' : 'WWT', 'email' : 'damon.watson@gmail.com', 'github_username' : 'hansolo107'}]

with open(r'C:\Users\watsond\Desktop\DevNet\damon_watson.yaml', 'w') as file:
    documents = yaml.dump(dict_file,file)
