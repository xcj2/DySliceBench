from collections import Counter,defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
a = inpl()
cnt = Counter(a)
res = 0
for v in cnt.values():
    if v - 1 > 0:
        res += v - 1
if res % 2:
    print(len(cnt)-1)
else:
    print(len(cnt))