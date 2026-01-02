def examC():
    C = [LI() for _ in range(3)]
    ans = "Yes"
    cur = [0]*3
    for i in range(2):
        cur[0] = C[0][i+1]-C[0][i]
        cur[1] = C[1][i+1]-C[1][i]
        cur[2] = C[2][i+1]-C[2][i]
        if not cur[0]==cur[1]==cur[2]:
            ans = "No"
    for i in range(2):
        cur[0] = C[i+1][0]-C[i][0]
        cur[1] = C[i+1][1]-C[i][1]
        cur[2] = C[i+1][2]-C[i][2]
        if not cur[0]==cur[1]==cur[2]:
            ans = "No"
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

examC()
