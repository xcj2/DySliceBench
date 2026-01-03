def examA():
    A, B, C = LI()
    S = A+B+C
    cur = 0
    for i in range(32):
        if A%2==1 or B%2==1 or C%2==1:
            break
        A = (S-A)//2
        B = (S-B)//2
        C = (S-C)//2
        cur +=1
    if cur==32:
        ans = -1
    else:
        ans = cur
    print(ans)

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
