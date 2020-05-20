#Day 1 - Quartiles
# Objective
# In this challenge, we practice calculating quartile
import sys

n = 1
x = []
an = 0
sol = []

print("Numero de Elementos: ")
n = int(input())
print("space separated arrays: ")
inpt = input()
data =  inpt.split()
x = [int(i, base=10) for i in data]
x.sort()
# x=inpt.separated()

an = len(x)

print()
print("Datos de Entrada")
print(n)
print(x)
print(an)
print()

if n != an :
    print("Wrong number of elements, please try again")
    sys.exit()
else :
    print ("continue")

# Lets Calculate

def fQuartiles(n, x):
    qvalue=[]
    y1=[]
    y2=[]

    if (n%2==0):
        print("It is even")
    else:
        print("It is Odd")
        #calculate mean=Q2
        q2=int(n/2-0.5)
        # q20=q2-1
        q21=q2+1
        y1=x[0:q2]
        y2=x[q21:]
        qvalue.append(x[q2])
        print(y1)
        print(y2)
        print(q2)
        # Now Calculate q1
        # Now Calculate q2
    return qvalue

sol=fQuartiles(n,x)
print()
print(sol)

