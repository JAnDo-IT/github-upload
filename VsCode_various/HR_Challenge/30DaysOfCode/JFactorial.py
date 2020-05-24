# Day 5 - Loop

def Loop(n):
    x=0
    y=1
    for i in range(n):
        x+=1
        y*=x
        print(x)
    
    return y

if __name__ == "__main__":
    n = int(input())
    print()
    if (n>=2 and n<=20):
        res=Loop(n)
        print()
        print(res)
    else:
        print("n out of calculation range")
