from collections import Counter,defaultdict,deque
from heapq import heapify,heappop,heappush
from bisect import bisect_left,bisect_right
import sys,math,itertools,string,queue
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
res = 0
def f(x):
    global res
    if x <= n:
        l = len(str(x))
        f(3*10**l+x)
        f(5*10**l+x)
        f(7*10**l+x)
        if '3' in str(x) and '5' in str(x) and '7' in str(x):
            res += 1
f(3)
f(5)
f(7)
print(res)