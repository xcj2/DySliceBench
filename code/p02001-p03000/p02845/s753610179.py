def examE(mod):
    N = I()
    A = LI()
    a =[0,0,0]
    cur = 1
    for i in A:
        if a[0]==i:
            if a[0]==a[1]:
                if a[1]==a[2]:
                    cur *= 3
                else:
                    cur *=2
            a[0]+=1
        elif a[1]==i:
            if a[1] == a[2]:
                cur *= 2
            a[1] +=1
        elif a[2]==i:
            a[2]+=1
        else:
            cur *=0
        a.sort(reverse=True)
        cur %=mod
    print(cur)
    return

def examF():
    return

import sys,copy,bisect,itertools,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examE(mod)
