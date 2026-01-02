def examA():
    X = I()
    if X<30:
        ans = "No"
    else:
        ans = "Yes"
    print(ans)
    return

def examB():
    N, D = LI()
    cnt = 0
    for _ in range(N):
        x, y = LI()
        if x**2+y**2<=D**2:
            cnt += 1
    ans = cnt
    print(ans)
    return

def examC():
    N = 10**7
    K = I()
    cur = 0
    now = 1
    ans = -1
    for i in range(N):
        cur += 7 * now
        cur %= K
        if cur==0:
            ans = i+1
            break
        now *= 10
        now %= K
    print(ans)
    return

def examD():
    N = I()
    C = SI()
    cnt = 0
    l = 0; r = N-1
    while(l<r):
        while(l<N):
            if C[l]=="W":
                break
            l += 1
        while(0<=r):
            if C[r]=="R":
                break
            r -= 1
        if l<r:
            cnt += 1
            l += 1
            r -= 1
    ans = cnt
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
global mod,mod2,inf,alphabet,_ep,alphabet_convert
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = dec("0.000000000001")
alphabet = [chr(ord('a') + i) for i in range(26)]
alphabet_convert = {chr(ord('a') + i): i for i in range(26)}

getcontext().prec = 28

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examD()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""