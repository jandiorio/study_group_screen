import yaml

#dictionary entries
profile_dict ={{'First Name' : ['Joel']},{'Last Name' : ['Byam']}, {'Company' : ['WWT']}, {'email' : ['joel.byam@wwt.com']}, {'github_username' : ['GroovyJ']}}

#write to yaml file
with open(r'C:\Users\byamj\Documents\Python\yaml\yaml_test_1.yaml', 'w') as file:
    yaml_test_1 = yaml.dump(multi_list_yaml,file)