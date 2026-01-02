import time
startTimeProblem=time.time()

import fileinput, sys, itertools, functools
from math import *
from bisect import *
from heapq import *
from collections import *
import queue

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

if M==0:
    Out.int(1)
else:
    conns = [set() for i in range(N)]
    for i in range(M):
        A, B = In.ints()

        A-=1
        B-=1

        if B not in conns[A]:
            conns[A].add(B)
        if A not in conns[B]:
            conns[B].add(A)
    
    ans = 0
    seen = set()
    for i in range(N):        
        if len(conns[i])==0:            
            continue
        
        if i not in seen:
            seen.add(i)

            #dfs
            stck = deque([(i)])
            ct = 1
            while len(stck)>0:
                now = stck.popleft()
                
                for nex in conns[now]:
                    if nex not in seen:
                        ct+=1
                        seen.add(nex)
                        ans = max(ans, ct)
                        stck.append(nex)
                    

    Out.int(ans)
        




######################################

if len(sys.argv)>2 and sys.argv[2]=="TIMEIT":
    fin = (time.time()-startTimeProblem)*1000
    print("{:.2f}".format(fin) + "ms")