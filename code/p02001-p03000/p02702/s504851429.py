def examA():
    S, W = LI()
    if S<=W:
        print("unsafe")
    else:
        print("safe")
    return

def examB():
    A, B, C, D = LI()
    while(True):
        C -= B
        if C<=0:
            print("Yes")
            break
        A -= D
        if A<=0:
            print("No")
            break
    return

def examC():
    N = I()
    S = [SI()for _ in range(N)]
    Set = set(S)
    ans = len(Set)
    print(ans)
    return

def examD():
    S = SI()
    N = len(S)
    D = [0]*(N+1)
    for i in range(N):
        D[i+1] = (D[i]+int(S[N-1-i])*pow(10,i,2019))%2019
    #print(D)
    ans = 0
    C = Counter(D)
    #print(C)
    for c in C.values():
        ans += (c-1)*c//2
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
    examD()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""