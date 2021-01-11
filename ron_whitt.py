import yaml
ronwhitt = [{"company":"WWT","email":"ron.whitt@wwt.com","first_name":"Ron","last_name":"Whitt","github_user":"ron-whitt"}]
with open("ronwhitt.yaml","w") as file:
  yaml.dump(ronwhitt, file)



