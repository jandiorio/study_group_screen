import yaml

file1 = open("patrick_laidlaw.yaml", "w")


mydict = {
    "first_name": "Patrick",
    "last_name": "Laidlaw",
    "company": "WWT",
    "email": "patrick.laidlaw@wwt.com",
    "github_username": "patricklaidlaw"
}

yaml.dump(mydict, file1)


file1.close()

#open and read the file after the appending:
f = open("patrick_laidlaw.yaml", "r")
print(f.read())