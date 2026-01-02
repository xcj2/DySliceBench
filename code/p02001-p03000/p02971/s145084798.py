from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,string,queue
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
a = inpln(n)
m = 0
mm = 0
cnt = 0
for i in a:
    if i > m:
        mm = m
        m = i
        cnt = 0
    elif i == m:
        cnt += 1
    elif i > mm:
        mm = i
for i in a:
    if i == m:
        if cnt > 0:
            print(m)
        else:
            print(mm)
    else:
        print(m)