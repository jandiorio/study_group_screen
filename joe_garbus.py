import yaml

#create dictionary

dictionary_test = [{
	"company" : "WWT", "email": "joe.garbus@wwt.com",
        "first_name" : "Joe", "github_username" : "Joe Garbus",
	"last_name" : "Garbus"
	}]

print (yaml.dump(dictionary_test))
