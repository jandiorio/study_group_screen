import yaml 
  
ali_list = [{'company':'WWT'}, {'email':'ali.rahi@wwt.com'}, {'first_name':'Ali'}, {'github_username':'alray79'}, {'last_name':'Rahi'}]

ali_dict = {}

for d in ali_list: ali_dict.update(d)

f = open("ali_rahi.yaml", "w")

yaml.dump(ali_dict, f)

f.close()
