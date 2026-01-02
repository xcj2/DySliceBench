from collections import Counter,defaultdict,deque
import sys,bisect,math,itertools,string,queue
from heapq import heappop, heappush
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
for i in range(1,10):
    for j in range(1,10):
        if i * j == n:
            print('Yes')
            quit()
print('No')