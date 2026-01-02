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
A = [0]+In.ints()

cur = 1
seen = set()
seen.add(cur)
circleStart = 0

i = 0
while i<K:
    cur = A[cur]

    if cur not in seen:
        seen.add(cur)
    else:
        circleStart = cur
        i+=1
        break
    i+=1

if i == K:
    Out.int(cur)
else:
    K-=i

    dist = dict()
    dist[0] = circleStart
    cur_dist = 0
    longest = 0

    i = 0
    while i<K:
        cur_dist+=1

        cur = A[cur]

        if cur!=circleStart:
            dist[cur_dist] = cur
            longest = max(cur_dist, longest)
        else:
            i+=1
            break

        i+=1

    if i == K:
        Out.int(cur)
    else:
        K-=i
        Out.int(dist[K%(longest+1)])


######################################

if len(sys.argv)>2 and sys.argv[2]=="TIMEIT":
    fin = (time.time()-startTimeProblem)*1000
    print("{:.2f}".format(fin) + "ms")