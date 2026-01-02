def examA():
    N = I()
    X = [LI()for _ in range(N)]
    l = 0; r = inf
    while(r-l>_ep):
        now = (l+r)/2
        x_l = -inf; x_r = inf
        y_l = -inf; y_r = inf
        for x,y,c in X:
            move = now / c
            x_l = max(x_l,x-move)
            x_r = min(x_r,x+move)
            y_l = max(y_l,y-move)
            y_r = min(y_r,y+move)
        if x_l<=x_r-_ep and y_l<=y_r-_ep:
            r = now
        else:
            l = now
    ans = r
    print(ans)
    return

def examB():
    N = I()
    C = LI()
    C.sort()
    base = pow(2,2*N-1,mod)
    inv = pow(2,mod-2,mod)
    ans = 0
    for i in range(N):
        cur = C[i]*base*(1+(N-1-i)*inv)
        ans += cur
        ans %= mod
    print(ans)
    return

def examC():
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
_ep = 10**(-9)
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