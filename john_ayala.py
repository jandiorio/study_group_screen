#!/usr/bin/env python3

import yaml

mylist = [
  {
    'first_name': "John",
    'last_name': "Ayala",
    'company': "WWT",
    'email': "john.ayala@wwt.com",
    'github_username': "johneayala"
  }
]

print(yaml.dump(mylist))

