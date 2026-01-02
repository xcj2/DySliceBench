import time
startTimeProblem=time.time()

import fileinput, sys, itertools, functools
from math import *
from bisect import *
from heapq import *
from collections import *

def lcm(a, b):  
    return (a*b)/gcd(a, b)

class InputHelper:
    def __init__(self):
        self.myinput = fileinput.input()

    def isLocal(self):
        return not fileinput.isstdin()

    def int(self):
        return int(self.myinput.readline().rstrip())

    def ints(self):
        return [int(_) for _ in self.myinput.readline().rstrip().split()]

    def str(self):
        return self.myinput.readline().rstrip()

    def strs(self):
        return [_ for _ in self.myinput.readline().rstrip().split()]

class OutputHelper:
    def int(self, a):
        print(a)    

    def ints(self, a):  
        print(" ".join([str(_) for _ in a]))
    
    def intsNL(self, a):
        for _ in a:
            print(_)
    
    def str(self, s):
        print(s)

    def strs(self, s):
        print(" ".join([_ for _ in s]))

    def strsNL(self, s):
        for st in s:
            print(st)

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

In = InputHelper()
Out = OutputHelper()

######################################

N, K = In.ints()

P = In.ints()
C = [-1] + In.ints()

connection = [-1 for i in range(N+1)]

for i in range(N):
    connection[i+1] = P[i]

ans = -99999999999

for i in range(1, N+1):
    start = connection[i]
    tempans = C[start]
    tempk = K-1

    ans = max(ans, tempans)
    seen = [False for i in range(N+1)]
    seen[start] = True    

    while tempk > 0:
        nex = connection[start]
        if not seen[nex]:
            start=nex
            seen[start]=True
            tempans += C[start]
            ans = max(ans, tempans)
            tempk-=1            
        else:
            break
    
    if tempk>N:
        if tempans<0:
            continue
        
        
        stepsround = K-tempk
        howManyRounds = (tempk//stepsround)-1

        tempans += tempans*howManyRounds
        tempk-=howManyRounds*stepsround

        ans = max(ans, tempans)
    
    while tempk > 0:        
        start=connection[start]            
        tempans += C[start]
        ans = max(ans, tempans)
        tempk-=1            



Out.int(ans)


######################################

if len(sys.argv)>2 and sys.argv[2]=="TIMEIT":
    fin = (time.time()-startTimeProblem)*1000
    print("{:.2f}".format(fin) + "ms")