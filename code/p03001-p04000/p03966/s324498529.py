from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
for i in range(n):
    a,b = inpl()
    if i == 0:
        x = a; y = b
        continue
    if x <= a and y <= b:
        x = a; y = b
        continue
    c = -(-x//a); d = -(-y//b)
    tmp = max(c,d)
    x = a*tmp; y = b*tmp
    # print(x,y)
print(x+y)
