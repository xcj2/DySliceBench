def examA():
    D,T,S = LI()
    if (D-1)//S<T:
        ans = "Yes"
    else:
        ans = "No"
    print(ans)
    return

def examB():
    S = SI()
    T = SI()
    s = len(S)
    t = len(T)
    ans = t
    for i in range(s-t+1):
        cnt = 0
        for j in range(t):
            if S[i+j]!=T[j]:
                cnt += 1
        ans = min(ans,cnt)

    print(ans)
    return

def examC():
    N = I()
    A = LI()
    S = sum(A)
    cnt = 0
    for a in A:
        cnt += (S-a)*a
        cnt %= mod
    ans = cnt * pow(2,mod-2,mod) % mod
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

from decimal import getcontext,Decimal as dec
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
_ep = dec("0.000000000001")
alphabet = [chr(ord('a') + i) for i in range(26)]
alphabet_convert = {chr(ord('a') + i): i for i in range(26)}

getcontext().prec = 28

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examC()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""