import time
startTimeProblem=time.time()

import fileinput, sys, itertools, functools, copy
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

N = In.int()
A = In.ints()
drueb = [defaultdict(int) for i in range(N)]

for i in range(N):
    # if i>=1:
    #     drueb[i] = copy.copy(drueb[i-1])
    val = i+1
    drueb[-1][A[i]-val] += 1

ans=0
for i in range(N):
    j = i+A[i]+1

    if j<len(drueb):
        if -A[i]-(i+1) in drueb[-1]:
            ans+=drueb[-1][-A[i]-(i+1)]
    
Out.int(ans)
        
######################################

if len(sys.argv)>2 and sys.argv[2]=="TIMEIT":
    fin = (time.time()-startTimeProblem)*1000
    print("{:.2f}".format(fin) + "ms")