def examA():
    L, R, D = LI()
    ans = R//D - (L-1)//D
    print(ans)
    return

def examB():
    N = I()
    A = LI()
    ans = 0
    for i,a in enumerate(A):
        if i%2==0:
            if a%2==1:
                ans += 1
    print(ans)
    return

def examC():
    N = I()
    ans = [0]*N
    for x in range(1,101):
        for y in range(1,101):
            for z in range(1,101):
                cur = x**2 + y**2 + z**2 + x*y + y*z + x*z
                if cur<N+1:
                    ans[cur-1] += 1

    for v in ans:
        print(v)
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

sys.setrecursionlimit(2*10**6)

if __name__ == '__main__':
    examC()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""