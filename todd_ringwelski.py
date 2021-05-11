
import yaml


student = {'first_name':'Todd','last_name':'Ringwelski','email':'todd.ringwelski@wwt.com','company':'World Wide Technology','github_username':'TRingo1'}

with open('todd.ringwelski.yaml', 'w') as outfile:
	yaml.dump(student, outfile, default_flow_style=False)
