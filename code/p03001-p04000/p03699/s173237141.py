def examC():
    N = I()
    s = [I() for _ in range(N)]
    is_trueScore = [False]*(max(s)*N+1)
    is_trueScore[0] = True
    ans = 0
    for i in s:
        for j in range(max(s)*N,i-1,-1):
            if is_trueScore[j-i]==True:
                is_trueScore[j]=True
    for i in range(max(s)*N+1):
        if i%10!=0:
            if is_trueScore[i]:
                ans = i
    print(ans)




import sys
import copy
import bisect
import heapq
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC()
