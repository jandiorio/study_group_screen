import yaml

brett = [{
        'first_name':'Brett',
        'last_name':'Millaway',
        'company':'WWT',
        'email':'brett.millaway@wwt.com',
        'github_username':'brettm92'
}]
        
brettstring=yaml.dump(brett)
f = open("output.yml", "w")
f.write(brettstring)
f.close()

