import yaml

dict_info = [dict(first_name='Michael', last_name='Bingham', company='WWT', email='michael.bingham@wwt.com',
                  github_username='blackbriar5405')]

print (yaml.dump(dict_info))
