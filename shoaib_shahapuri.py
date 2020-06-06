#!/usr/bin/env python

#import dump function from PyYAML to convert python list into yaml file
from yaml import dump

#define variable with  basic info
basic_info = [
              {
               "company": "WWT",
               "email": "shoaibmohammed.shahapuri@wwt.com",
               "first_name": "Shoaib",
               "github_username": "sh271011",
               "last_name": "Shahapuri" 
               }
             ]

#use dump module to convert python variable to a yaml format
data = "---\n" + dump(basic_info, default_flow_style=False)

#create a new file and write the data
with open("basic_info.yml", "w") as f:
 f.write(data)

#End of File

