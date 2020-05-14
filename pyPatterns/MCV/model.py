## Model
# It consists of pure application logic, which interacts with the database.
# It includes all the information to represent data to the end user.
# Py:
# Let us consider a basic object called “Person” and create an MVC design pattern.

import json

class Person(object):
   def __init__(self, first_name = None, last_name = None):
      self.first_name = first_name
      self.last_name = last_name
   #returns Person name, ex: John Doe
   def name(self):
      return ("%s %s" % (self.first_name,self.last_name))
		
   @classmethod
   #returns all people inside db.txt as list of Person objects
   def getAll(self):
      """ seems py2 style
      database = open('db.txt', 'r')
      result = []
      json_list = json.loads(database.read())
      """
      #filename = "C:\Local\PythonGit-J\pyPatterns\MCV\jandofile.txt"
      filename = "C:\Local\PythonGit-J\pyPatterns\MCV\db.txt"

      result = []
      myfile = open(filename, 'r')
      #json_list = json.loads(myfile.readlines())
      json_list = myfile.read().splitlines()
      print(json_list)
      #with open(filename) as database:
      #  json_list = database.read().splitlines()
      print()

      for item in json_list:
         # json.loads()
         item = json.loads(item)
         # item = json.dumps(item)
         person = Person(item['first_name'], item['last_name'])
         # person = Person(item[0], item[1])
         result.append(person)

      return result

