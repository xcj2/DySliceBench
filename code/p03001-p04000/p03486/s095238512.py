def examB():
    St = S(); T = S()
    s_asc = ''.join(sorted(St))
    t_desc = ''.join(sorted(T, reverse=True))
    if s_asc < t_desc:
        print('Yes')
    else:
        print('No')


import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examB()
