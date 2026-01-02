def examD(mod):
    N = I(); A = LI()
    d = defaultdict(int)
    for i in range(N):
        cur = A[i]
        j = 1
        while(cur>0):
            if cur&1==1:
                d[j] +=1
            j +=1
            cur >>=1
    ans = 0
    for i,j in d.items():
        ans += j*(N-j) * 2**(i-1)
        ans %=mod
    print(ans)
    return

def examE():
    return

def examF():
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

if __name__ == '__main__':
    examD(mod)
