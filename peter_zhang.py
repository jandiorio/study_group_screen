#!/usr/bin/env python3

import yaml
import json

class WWTEmployee(object):
    company = 'WWT'
    def __init__(self, f_name, l_name, email, gh_username):
        self.employee_info = [{
            'Company': self.company,
            'email':email,
            'first_name':f_name,
            'last_name':l_name,
            'github_username': gh_username
        }]

    def output_yaml(self):
        return yaml.dump(self.employee_info)
    
    def output_json(self):
        return json.dumps(self.employee_info, indent=4)

def main():
    f_name = 'Peter'
    l_name = 'Zhang'
    email = 'peter.zhang@wwt.com'
    gh_username = "ACISupport"
    init_employee = WWTEmployee(f_name, l_name, email, gh_username)
    with open ('employees.yml', 'r+') as yml_file:
        employees = yaml.load(yml_file, Loader=yaml.FullLoader)
        try:
            for employee in employees:
                if employee['email'] == email:
                    print (f"Employee with email {email} already exists in the system")
                    break
            else:
                yml_file.write(f"{init_employee.output_yaml()}")
        except TypeError:
            yml_file.write(f"{init_employee.output_yaml()}")

if __name__ == "__main__":
    main()