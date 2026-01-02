def examA():
    N = I()
    ans = 0
    print(ans)
    return

def examB():
    N, M = LI()
    P = [0]*N
    S = [LSI()for _ in range(M)]
    pena = 0
    ac = set()
    for p,s in S:
        p = int(p)-1
        if s=="WA":
            P[p] += 1
        else:
            if p in ac:
                continue
            ac.add(p)
            pena += P[p]

    print(len(ac),pena)
    return

def examC():
    ans = 0
    print(ans)
    return

def examD():
    ans = 0
    print(ans)
    return

def examE():
    ans = 0
    print(ans)
    return

def examF():
    ans = 0
    print(ans)
    return

import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(readline())
def LI(): return list(map(int,readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examB()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""