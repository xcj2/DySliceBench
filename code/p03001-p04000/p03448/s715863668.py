def examB():
    A = I(); B = I(); C = I(); X = I()
    ans = 0
    for i in range(min(41,A+1)):
        for j in range(B+1):
            for k in range(C+1):
                cur = 500*i + 100*j + 50*k
                if cur==X:
                    ans +=1
    print(ans)

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examB()
