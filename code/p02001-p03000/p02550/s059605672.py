import time
startTimeProblem=time.time()

import fileinput, sys, itertools, functools, copy, math
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

N, X, M = In.ints()

ans = 0
steps = 1
seen = dict()
stepsseen = dict()
stepsseen[0] = 0

while X != 0 and N>0 and X not in seen:    
    ans += X
    seen[X] = (ans, steps)
    stepsseen[steps] = ans
    X = (X**2)%M
    N-=1
    steps+=1


if X not in seen:
    Out.int(ans)
else:
    stepsDiff = steps-seen[X][1]
    ansDiff = ans-stepsseen[seen[X][1]-1]

    remloops = N//stepsDiff
    N = N%stepsDiff

    ans += remloops*ansDiff

    while X != 0 and N>0:    
        ans += X
        X = (X**2)%M
        N-=1
    
    Out.int(ans)


######################################

if len(sys.argv)>2 and sys.argv[2]=="TIMEIT":
    fin = (time.time()-startTimeProblem)*1000
    print("{:.2f}".format(fin) + "ms")