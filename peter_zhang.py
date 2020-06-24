#!/usr/bin/env python3

import yaml
import json

class WWTEmployeeDirectory(object):
    company = 'WWT'
    def __init__(self):
        self.employee_info = []

    def add_employee(self, f_name, l_name, email, gh_username):
        return self.employee_info.append({
            'Company': self.company,
            'email':email,
            'first_name':f_name,
            'last_name':l_name,
            'github_username': gh_username
        })

    def output_yaml(self):
        return yaml.dump(self.employee_info)
    
    def output_json(self):
        return json.dumps(self.employee_info, indent=4)

def main():
    f_name = 'Peter'
    l_name = 'Zhang'
    email = 'peter.zhang@wwt.com'
    gh_username = "ACISupport"
    employee_directory = WWTEmployeeDirectory()
    employee_directory.add_employee('peter', 'zhang', 'peter.zhang@wwt.com', 'ACISupport' )
    with open ('employees.yml', 'r+') as yml_file:
        employees = yaml.load(yml_file, Loader=yaml.FullLoader)
        try:
            for employee in employees:
                if employee['email'] == email:
                    print (f"Employee with email {email} already exists in the system")
                    break
            else:
                yml_file.write(f"{employee_directory.output_yaml()}")
        except TypeError:
            yml_file.write(f"{employee_directory.output_yaml()}")

if __name__ == "__main__":
    main()