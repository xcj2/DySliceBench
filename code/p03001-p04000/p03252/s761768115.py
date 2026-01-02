def examA():
    A = LI()
    A.sort()
    ans = A[2]*10+A[1]+A[0]
    print(ans)
    return

def examB():
    N, M, x, y = LI()
    X = LI()
    Y = LI()
    X.sort(); Y.sort()
    if max(X[-1],x)<min(Y[0],y):
        print("No War")
    else:
        print("War")
    return

def examC():
    S = SI()
    T = SI()
    N = len(S)
    Ds = defaultdict(str)
    Dt = defaultdict(str)
    for i in range(N):
        s = S[i]; t = T[i]
        if Ds[s]!="" and Ds[s]!=t:
            print("No")
            return
        Ds[s] = t
        if Dt[t] != "" and Dt[t] != s:
            print("No")
            return
        Dt[t] = s
    print("Yes")
    return

def examD():
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
def I(): return int(input())
def LI(): return list(map(int,sys.stdin.readline().split()))
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