def examA():
    K = I()
    A, B = LI()
    for i in range(A,B+1):
        if i%K==0:
            print("OK")
            return
    print("NG")
    return

def examB():
    X = I()
    now = 100
    ans = 0
    while(now<X):
        ans += 1
        now += now//100
    print(ans)
    return

def examC():
    N, M, Q = LI()

    ans = 0
    print(ans)
    return

def examD():
    A, B, N = LI()
    if N>=B-1:
        ans = (A*(B-1))//B
    else:
        ans = (A*N)//B
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
def LI(): return list(map(int, sys.stdin.readline().split()))
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