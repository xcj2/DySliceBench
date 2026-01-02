from collections import Counter,defaultdict,deque
import sys,bisect,math,itertools,string,queue
from heapq import heappop, heappush
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n,m,k = inpl()
bla = 0
for i in range(n+1):
    bla = i*m
    for j in range(m+1):
        if bla + (n-2*i) * j == k:
            print('Yes')
            quit()
print('No')
