'''
Creates a list of dictionaries with a single dictionary
dictionary will have the following keys: ['first_name', 'last_name', 'company', 'email', 'github_username']
dictionary will have your information as the values
convert the list to a YAML string
write the YAML string to a file
'''

list_of_dicts = [{'company': 'WWT', 'email': 'jimmy.copeland@wwt.com', 'first_name': 'Jimmy', 
                  'last_name': 'Copeland', 'github_username': 'jmctm'}]
                  
yaml_output_string = ''


def create_yaml_string(dict_to_parse):
    '''
    Will read the dictionary and then create the yaml string 
    
    Returns:
        yaml string
    '''
    first_line = True
    return_string = ''
    for key in dict_to_parse.keys():
        if first_line:
            return_string = f'- {key}: {dict_to_parse[key]}\n'
            first_line = False
        else:
            return_string += f'  {key}: {dict_to_parse[key]}\n'
    return return_string
    
    
yaml_output_string = create_yaml_string(list_of_dicts[0])
            
yaml_output_file_name = f"{list_of_dicts[0]['first_name']}_{list_of_dicts[0]['last_name']}.yaml"
            
yaml_output_file = open(yaml_output_file_name, 'w')
yaml_output_file.write(yaml_output_string)
yaml_output_file.close()
