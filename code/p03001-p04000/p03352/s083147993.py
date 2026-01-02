def pff(m):
    pf = {}
    for i in range(2, int(m ** 0.5) + 1):
        while m % i == 0:
            pf[i] = pf.get(i, 0) + 1
            m //= i
    if m > 1: pf[m] = 1
    return pf
def examB():
    X = I()
    ans = 0
    for i in range(X,0,-1):
        cur = pff(i)
        flag = True
        now = 0
        for j in cur.values():
            if j==1:
                flag = False
            if now==0:
                now = j
            else:
                if now!=j:
                    flag = False
        if flag:
            ans = i
            break
    print(ans)

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examB()