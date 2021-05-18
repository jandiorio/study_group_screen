#!/usr/bin/env python3
import yaml

with open('Pyadav.yml') as f:
    
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(yaml.dump(data))