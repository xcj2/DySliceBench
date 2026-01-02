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

N, M, Q = In.ints()


fromTo = defaultdict(list)

for i in range(Q):
    a, b, c, d = In.ints()

    fromTo[a].append((b,c,d))

ans = 0

def rec(arr,N,M,fromTo):
    if len(arr)==N:
        points = 0

        for i in range(len(arr)):
            idx = i+1
            if idx in fromTo:
                for rule in fromTo[idx]:
                    b,c,d = rule
                    if arr[b-1]-arr[i]==c:
                        points+=d
        global ans
        ans = max(ans, points)
        return

    highest = arr[-1]

    for i in range(highest, M+1):
        arr.append(i)
        rec(arr,N,M,fromTo)
        arr.pop(-1)


rec([1],N,M,fromTo)


Out.int(ans)

######################################

if len(sys.argv)>2 and sys.argv[2]=="TIMEIT":
    fin = (time.time()-startTimeProblem)*1000
    print("{:.2f}".format(fin) + "ms")