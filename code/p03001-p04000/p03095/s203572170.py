def examA(mod):
    N = I(); S = SI()
    d = defaultdict(int)
    ans = 1
    for s in S:
        d[s] +=1
    for i in d.values():
        ans *=(i+1)
    print((ans-1)%mod)

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
    examA(mod)