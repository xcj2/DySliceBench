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

H, W = In.ints()

grid = [["." for j in range(W)] for i in range(H)]

C = In.ints()
C = (C[0]-1, C[1]-1)
D = In.ints()
D = (D[0]-1, D[1]-1)

for i in range(H):
    s = In.str()

    for j in range(W):
        grid[i][j] = s[j]    

#print(grid)

moves = [[0,1], [0,-1], [1,0], [-1,0]]
setnext = set()
setnow = set([(C[0], C[1])])
quenow = deque([(C[0], C[1])])

ans = 0
found = False
hadOne = True

while hadOne:
    hadOne=False
    while len(quenow)>0:
        hadOne=True
        now = quenow.popleft()

        for i in range(-2,3):
            for j in range(-2, 3):
                nex = (now[0]+i, now[1]+j)

                if 0<=nex[0]<H and 0<=nex[1]<W and grid[nex[0]][nex[1]]==".":
                    if nex not in setnow and nex not in setnext:
                        setnext.add(nex)                    

        for m in moves:
            nex = (now[0]+m[0], now[1]+m[1])

            if nex == D:
                found = True
                break

            if 0<=nex[0]<H and 0<=nex[1]<W and grid[nex[0]][nex[1]] == "." and nex not in setnow:
                quenow.append(nex)
                setnow.add(nex)
        
        if found:
            break
    
    if found:
        break
    
    ans += 1

    for el in setnext:
        if el==D:
            found=True
            break
        if el not in setnow:            
            setnow.add(el)
            quenow.append(el)
    
    setnext.clear()
    
    if found:
        break


if found:
    Out.int(ans)
else:
    Out.int(-1)
######################################

if len(sys.argv)>2 and sys.argv[2]=="TIMEIT":
    fin = (time.time()-startTimeProblem)*1000
    print("{:.2f}".format(fin) + "ms")