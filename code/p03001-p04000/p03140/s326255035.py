def examB():
    N = I()
    A = SI(); B = SI(); C = SI()
    ans = 2*N
    for i in range(N):
        cur = 0
        if A[i]==B[i]:
            cur +=1
        if B[i]==C[i]:
            cur +=1
        if C[i]==A[i]:
            cur +=1
        ans -=min(2,cur)
    print(ans)
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
    examB()
