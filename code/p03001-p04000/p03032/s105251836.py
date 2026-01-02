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
V = In.ints()

class Solution():
    def __init__(self, K, V):
        self.ans = 0
        self.k = K
        self.posSum = 0
        self.negPreSum = [0]
        self.V = V

    @functools.lru_cache(None)
    def rec(self, fromIncl, toIncl):
        self.k -= 1
        canCallNext = self.k>0 and fromIncl!=toIncl

        #taketh left part
        leftVal = self.V[fromIncl]
        if leftVal>=0:
            self.posSum+=leftVal
        else:
            bipos = bisect_left(self.negPreSum, -leftVal)
            self.negPreSum.insert(bipos, -leftVal)

        negIdx = max(len(self.negPreSum)-1-self.k, 0)
        self.ans = max(self.ans, self.posSum-sum(self.negPreSum[0:negIdx+1]))

        if canCallNext:
            self.rec(fromIncl+1, toIncl)
        
        if leftVal>=0:
            self.posSum-=leftVal
        else:
            self.negPreSum.pop(bipos)
        
        #taketh right
        rightVal = self.V[toIncl]
        if rightVal>=0:
            self.posSum+=rightVal
        else:
            bipos = bisect_left(self.negPreSum, -rightVal)
            self.negPreSum.insert(bipos, -rightVal)

        negIdx = max(len(self.negPreSum)-1-self.k, 0)
        self.ans = max(self.ans, self.posSum-sum(self.negPreSum[0:negIdx+1]))

        if canCallNext:
            self.rec(fromIncl, toIncl-1)

        if rightVal>=0:
            self.posSum-=rightVal
        else:
            self.negPreSum.pop(bipos)

        self.k += 1


sol = Solution(K, V)
sol.rec(0, N-1)
Out.int(sol.ans)

######################################

if len(sys.argv)>2 and sys.argv[2]=="TIMEIT":
    fin = (time.time()-startTimeProblem)*1000
    print("{:.2f}".format(fin) + "ms")