import yaml
dict = [{'company':'WWT','email':'Jayce.Graham@wwt.com','first_name':'Jayce','github_username':'jjsastra','last_name':'Graham'}]
# ref: https://stackoverflow.com/questions/31745159/how-to-combine-a-list-of-dictionaries-to-one-dictionary
with open('dict7.yml', 'w') as outfile:
	yaml.dump(dict, outfile, default_flow_style=False)
# I am not this smart: https://stackoverflow.com/questions/12470665/how-can-i-write-data-in-yaml-format-in-a-file