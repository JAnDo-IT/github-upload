# simple main funct with class

class person:
    def __init__ (self, name=None, age=None):
        self.name=name
        self.age=age
    def jprint(self):
        print(self.name)
        print(self.age)

def main():
    print ("Hallo Pishi Yisus")
    pJ = person("Yisus", 51)
    pJ.jprint()

funa = __name__

print( "The function is: {} ".format(funa) )

# Old but useful style
if __name__ == funa:
    main()

#New Python3 style Totally useful
# main()

