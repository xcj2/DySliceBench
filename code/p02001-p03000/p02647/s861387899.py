def examA():
    S = SI()
    ans = S[:3]
    print(ans)
    return

def examB():
    A, V = LI()
    B, W = LI()
    T = I()
    L = abs(A-B)
    v = V-W
    if v*T>=L:
        ans = "YES"
    else:
        ans = "NO"
    print(ans)
    return

def examC():
    N, K = LI()
    A = LI()
    for _ in range(min(60,K)):
        cur = N
        L = [0] * (N + 1)
        R = [0] * (N + 1)
        for i in range(N):
            a = A[i]
            if 0<i-a:
                L[i-a] += 1
            else:
                L[0] += 1
            if N>i+a+1:
                R[i+a+1] += 1
            else:
                R[N] += 1
            if cur>a:
                cur = a
        if cur==N:
            break
        A[0] = L[0]
        for i in range(1,N):
            A[i] = A[i-1]+L[i]-R[i]


    print(" ".join(map(str,A)))
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

def test():
    i = I()
    li = LI()
    lsi = LSI()
    si = LS()
    print(i)
    print(li)
    print(lsi)
    print(si)
    return

from decimal import Decimal as dec
import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(input())
def LI(): return list(map(int,sys.stdin.readline().split()))
def DI(): return dec(input())
def LDI(): return list(map(dec,sys.stdin.readline().split()))
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