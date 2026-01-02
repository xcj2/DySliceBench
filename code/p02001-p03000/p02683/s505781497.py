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

N, M, X = In.ints()

cost = [0]*N
ach = [[0 for i in range(M)] for j in range(N)]

for i in range(N):
    ine = In.ints()
    cost[i] = ine[0]
    ach[i] = ine[1::]

res = 99999999999


for i in range(N):            
    for comb in itertools.combinations([i for i in range(N)], i+1):        
        cur_cost = 0
        accum = [0]*M

        for el in comb:
            cur_cost+=cost[el]

            for j in range(M):
                accum[j] += ach[el][j]

            if all([x>=X for x in accum]):
                found=True
                res = min(res, cur_cost)
                break


if res == 99999999999:
    Out.int(-1)
else:
    Out.int(res)

######################################

if len(sys.argv)>2 and sys.argv[2]=="TIMEIT":
    fin = (time.time()-startTimeProblem)*1000
    print("{:.2f}".format(fin) + "ms")