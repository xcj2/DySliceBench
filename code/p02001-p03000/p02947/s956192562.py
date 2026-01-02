def examA():
    N = I()
    L = LI()
    L.sort()
    if sum(L)<=L[-1]*2:
        print("No")
    else:
        print("Yes")
    return

def examB():
    N, M = LI()
    A = [LI()for _ in range(N)]
    A.sort(key=lambda x:x[0])
    ans = 0
    for a,b in A:
        if M<=b:
            ans += a*M
            break
        ans += a*b
        M -= b
    print(ans)
    return

def examC():
    N = I()
    S = [SI()for _ in range(N)]
    D = defaultdict(int)
    for s in S:
        cur = []
        for i,j in Counter(s).items():
            cur.append((i,j))
        #print(cur)
        cur.sort()
        cur = tuple(cur)
        D[cur] += 1
    ans = 0
    for d in D.values():
        ans += (d-1)*d//2
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
    examC()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""