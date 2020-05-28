# Enter your code here. Read input from STDIN. Print output to STDOUT
class clasify:
    separate=[]
    def __init__(self, pyWord):
        self.separate=pyWord
    
    def operate(self):
        #print(self.separate)
        for sep in self.separate:
            jwordo= ""
            jworde= ""
            dist=len(sep)
            for i in range(dist):
                if i==0:
                    jworde+=sep[i]
                elif i%2==0:
                    jworde+=sep[i]
                else:
                    jwordo+=sep[i]
                # print(sep[i])
            print(jworde, jwordo)

if __name__ == "__main__":
    t = int(input())
    pyWord = []
    for i in range(t):
        word=input()
        pyWord.append(word)
        #print("test: ", i)
        #print(pyWord[i])
    
    solve=clasify(pyWord)
    solve.operate()
