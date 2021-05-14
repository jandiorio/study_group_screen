

mydata = {"Company": "Truist", "Email": "donald.furr@truist.com", "First_Name": "Donald", "GitHub_Username": "dfurr2000", "Last_Name": "Furr"}
import yaml
print (yaml.dump(mydata))
filepath = "c:\donald_furr.yaml"
with open('donald_furr.yaml', 'w') as file:
    yaml.dump(mydata, file)


