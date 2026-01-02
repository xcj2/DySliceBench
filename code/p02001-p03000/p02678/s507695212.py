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

N, M = In.ints()

conn = [set() for j in range(N+1)]

for i in range(M):
    A, B = In.ints()

    conn[A].add(B)
    conn[B].add(A)

que = deque([1])
selection = [0]*(N+1)
seen = set([1])

while len(que)>0:
    el = que.popleft()

    for nextVert in conn[el]:
        if nextVert not in seen:
            selection[nextVert] = el 
            seen.add(nextVert)
            que.append(nextVert)

Out.str("Yes")
for i in range(2, len(selection)):
    Out.int(selection[i])

######################################

if len(sys.argv)>2 and sys.argv[2]=="TIMEIT":
    fin = (time.time()-startTimeProblem)*1000
    print("{:.2f}".format(fin) + "ms")