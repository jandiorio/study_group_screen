#!/bin/bash/env python3
import yaml
#DevNet Study Group Skills Check - BASIC script
#ChrisLuntsford
def profile():
    list_p = ['f_name', 'l_name','g_name', 'c_name', 'e_name']
    list_s = ['first name: ', 'last name: ', ' github username: ', 'company name: ', 'email address: ']
    list_k =['first_name', 'last_name', 'github_username', 'company', 'email']
    list_v = []
    for p, s in zip(list_p, list_s):
        p = input(f'Please enter your {s}')
        list_v.append(p)
    #test List
    """for v in list_v:
        print(v)"""
    profile_dict = {}
    for  k, v in zip(list_k, list_v):
        profile_dict[k] = v
    # test dictionary
    #print(profile_dict)
    # test iteration through dictionary
    """for key, value in profile_dict.items():
        print(key, value)"""
    list_y = [profile_dict]

    # YAML Ain't Markup Language conversion happens here, thanks PYAML
    #Print yaml string
    print(yaml.dump(list_y, sort_keys=False))
    #write to yaml file
    with open("profile.yaml", "w") as fh:
        yaml.dump(list_y, fh)



def main():
    profile()

if __name__ == '__main__':
    main()
