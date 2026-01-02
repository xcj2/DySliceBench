from collections import Counter,defaultdict,deque
from heapq import heapify,heappop,heappush
import sys,bisect,math,itertools,string,queue
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
a = inpl()
res = []
for i in range(n):
    for j in range(len(a))[::-1]:
        # print(j)
        if a[j] > j+1:
            print(-1)
            quit()
        elif a[j] == j+1:
            res.append(a[j])
            del a[j]
            break
    # print(a)
for i in range(n)[::-1]:
    print(res[i])

