# Day 5 - Loop
def Loop(n):
    i=1
    y=1
    r=10
    for i in range(r):
        i+=1
        y=n*i
        print("{} x {} = {}".format(n, i, y))
    
    return y

if __name__ == "__main__":
    n = int(input())
    #print()
    if (n>=2 and n<=20):
        res=Loop(n)
        #print()
        #print(res)
    else:
        print("n out of calculation range")
