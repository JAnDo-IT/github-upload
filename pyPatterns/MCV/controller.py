"""
Controller
It acts as an intermediary between view and model. 
It listens to the events triggered by view and queries model for the same.
Py:
Controller interacts with model through the getAll() method which fetches 
all the records displayed to the end user.
"""
from model import Person
import view

def showAll():
   #gets list of all Person objects
   people_in_db = Person.getAll()
   #calls view
   return view.showAllView(people_in_db)

def start():
   view.startView()
   ## input = raw_input()  ##Seems Py 2
   vIn = input(" J Response: ")
   vIn.upper()
   # if input == 'y':
   
   if vIn == 'y':
      return showAll()
   else:
      return view.endView()

if __name__ == "__main__":
   #running controller function
   start()
