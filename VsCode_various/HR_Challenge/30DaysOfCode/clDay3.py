class WeirdNot:
    n=0
    def __init__(self, n):
        self.n = n

    def sConditional(self):
        n=self.n
        if (n%2 != 0):
            print("Weird")
        elif (n%2 == 0): #Checking only once
            if (n>=2 and n<=5):
                print("Not Weird")
            elif (n>=6 and n<=20):
                print("Weird")        
            elif (n>20):
                print("Not Weird")
            else:
                pass
        else:
            print("Not evaluated")
def main(N):
    cond = WeirdNot(N)
    cond.sConditional()

if __name__ == "__main__":
    N = int(input())
    if N>= 1 and N<=100:
        main(N)
    else:
        print("value not in range: try again")