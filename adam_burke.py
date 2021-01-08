# DevNet study group screen
import yaml

#create dictionary
ab_dict = {'company': 'WWT', 'email': 'adam.burke@wwt.com', 'first_name': 'Adam', 'github_username': 'atburke85', 'last_name': 'Burke'}

#Generate YAML
yaml_output = yaml.dump(ab_dict, default_flow_style=False)

#Create YAML file, write content, then close
print_file = open("adam_burke.yaml", "w")
print_file.write(yaml_output)
print_file.close()

# Remove output testing
# print (yaml_output)