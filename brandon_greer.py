import yaml

def dump_yaml(info_dict):
    '''
    Creates a yaml file called 'brandon_greer.yaml', then dumps the received dict into it as
    a list.
    '''
    with open('brandon_greer.yaml', 'w+') as dump_file:
        # Dump dictionary to file, but first wrap it into a list
        dump_file.write(yaml.safe_dump([info_dict]))

def main():

    # Create dictionary
    info_dict = {
        'first_name': 'Brandon',
        'last_name': 'Greer',
        'github_username': 'ccnPeon',
        'company': 'Arista Networks',
        'email': 'bmgreer09@gmail.com'
        }

    # Call dump_yaml function that will dump the dictionary to yaml
    dump_yaml(info_dict)


if __name__ == '__main__':
    main()