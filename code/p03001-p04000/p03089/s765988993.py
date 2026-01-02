def examA():
    N = I()
    B = LI()
    ans = [0]*N
    flag = False
    for i in range(N-1,-1,-1):
        for j in range(i,-1,-1):
            if j+1==B[j]:
                ans[i] = B[j]
                del B[j]
                break
        if ans[i]==0:
            print("-1")
            flag = True
            break
    if not flag:
        for v in ans:
            print(v)

from string import digits
import sys,copy,bisect,itertools,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examA()
