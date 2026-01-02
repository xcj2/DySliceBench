def examD():
    N = I()
    A = LI(); A.sort()
    ans = [max(A)]
    ansC = ans[0]/2
    lower = 0; upper = N-2
    while(upper-lower>1):
        now = (lower+upper)//2
        if A[now]>ansC:
            upper = now
        elif A[now]<ansC:
            lower = now
        else:
            ans.append(int(ansC))
            break
    if len(ans)==1:
        if abs(A[upper]-ansC)-abs(A[lower]-ansC)<0:
            now = upper
        else:
            now = lower
        ans.append(A[int(now)])
    print(" ".join(map(str,ans)))


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

examD()
