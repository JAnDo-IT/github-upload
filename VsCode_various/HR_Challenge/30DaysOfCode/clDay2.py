#Meal Calculations + tip + tax
fn = __name__

class meal:
    msg=""
    mealCost=0.0
    tip=0
    tax=0

    def __init__ (self, mealCost, tip, tax):
        self.msg=" Class Meal "
        self.mealCost=mealCost
        self.tip=tip
        self.tax=tax

    def oper(self):
        #print("from: " + self.msg )
        mTip = self.mealCost*(self.tip/100)
        mTax = self.mealCost*(self.tax/100)
        mealTotal = self.mealCost + mTip + mTax
        total = round(mealTotal)
        return total

def main():
    mealCost= float(input())
    tipPercent = int(input())
    taxPercent = int(input())

    #mealCost= float(input("Cost: $"))
    #tipPercent = int(input("tip: "))
    #taxPercent = int(input("tax: "))

    scramble = meal(mealCost, tipPercent, taxPercent)
    #print(scramble.oper() )
    total=scramble.oper()    
    print(total)

if __name__ == fn :
    #print("from name ")
    main()

#print("from principal: " + fn)
