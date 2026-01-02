def examA():
    H1, M1, H2, M2, K = LI()
    T = (H2-H1)*60 + (M2-M1)
    ans = T-K
    print(ans)
    return

def examB():
    T = SI()
    ans = ""
    for t in T:
        if t=="?":
            ans += "D"
        else:
            ans += t
    print(ans)
    return

def examC():
    N = I()
    A = LI()
    check = 1<<N
    for i,a in enumerate(A):
        check -= (1<<(N-i))*a
    if check<0:
        print(-1)
        return
    ans = 0
    cnt = 1
    less = sum(A)
    for i in range(N+1):
        a = A[i]
        if cnt>less:
            cnt = less
        ans += cnt
        less -= a
        cnt = (cnt-a)*2
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