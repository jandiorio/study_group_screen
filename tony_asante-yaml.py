import yaml

if _name_ == '_main_': 

   stream = open("tony_asante.yaml", 'r')
   dictionary = yaml.load(stream)
   for key, value in dictionary.items():
       print (key + " ; " + str(value))
