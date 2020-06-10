#!/usr/bin/env/python3

import yaml

about_me_list = [
    {
        'first_name':'Timothy',
        'last_name':'Hull',
        'company':'WWT',
        'email':'timothy.hull@wwt.com',
        'github_username':'timothyhull',
    }
]

with open('timothy_hull.yaml', 'w') as file:
    file.write(yaml.safe_dump(about_me_list))
