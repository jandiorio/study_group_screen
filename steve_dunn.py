import yaml

my_list = [{'first_name':'Steve'}, {'last_name':'Dunn'}, {'company':'WWT'}, {'email':'steve.dunn@wwt.com'}, {'github_username':'stevdunn'}]
my_dict = {}

for d in my_list: my_dict.update(d)

print(yaml.dump(my_dict, explicit_start=True, default_flow_style=False), file=open("output.txt", "a"))

