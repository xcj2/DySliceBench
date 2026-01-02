def examA():
    N = I()
    if N%2==1:
        print("Red")
    else:
        print("Blue")
    return

def examB():
    N, M = LI()
    D = [True]*M
    for _ in range(N):
        A = LI()
        cur = [False]*M
        for a in A[1:]:
            cur[a-1] = True
        for i in range(M):
            if not cur[i]:
                D[i] = False
    ans = 0
    for d in D:
        if d:
            ans += 1
    print(ans)
    return

def examC():

    return

def examD():

    return

import sys,copy,bisect,itertools,heapq,math,random
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
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

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    examB()

"""

"""