import yaml

#dictionary entries
profile_dict =[{'First Name' : ['Joel']},{'Last Name' : ['Byam']}, {'Company' : ['WWT']}, {'email' : ['joel.byam@wwt.com']}, {'github_username' : ['GroovyJ87']}]

#write to yaml file
with open(r'C:\Users\byamj\Documents\Python\yaml\joel_byam.yaml', 'w') as file:
    yaml_output = yaml.dump(profile_dict,file)