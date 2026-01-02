def examA():
    C1 = SI()
    C2 = SI()
    ans = "YES"
    if C1[0]!=C2[2] or C1[1]!=C2[1] or C1[2]!=C2[0]:
        ans = "NO"
    print(ans)
    return

def examB():
    A, B, C, X, Y = LI()
    loop = max(X,Y)
    ans = inf
    for i in range(loop+1):
        cost = i*2*C
        if X>i:
            cost += A*(X-i)
        if Y>i:
            cost += B*(Y-i)
        ans = min(ans,cost)
    print(ans)
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
    examB()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""