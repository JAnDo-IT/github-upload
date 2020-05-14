## View
# represents the HTML files, which interact with the end user. 
# It represents the model’s data to user.
# Py:
# It displays all the records fetched within the model. 
# View never interacts with model; controller does this work (communicating with model and view).

from model import Person
def showAllView(list):
   print ('In our db we have %i users. Here they are:' % len(list))
   for item in list:
      print (item.name())
def startView():
   print ('MVC - the simplest example' )
   print ('Do you want to see everyone in my db?[y/n]' )
def endView():
   print ('Goodbye!')


