import math
import os
import random
import re
import sys

class solverev():
    arrev=[]
    def __init__ (self, arr):
        self.arrev = arr
    
    def doreverse(self):
        restr=""
        dist=0
        jarr = self.arrev
        jarr.reverse()
        dist=len(jarr)
        # restr=
        for s in jarr:
           restr+=str(s)
           restr+=" "
        print(restr)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    # print(arr)
    solve = solverev(arr)
    solve.doreverse()

    # arr.reverse()
    # print(arr)


