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
d = defaultdict(int)
for i in a:
    d[i//400] += 1
c = 0
f = 0
for key in d.keys():
    if key < 8:
        c += 1
    else:
        f += d[key]
if c == 0:
    print(1,f)
else:
    print(c,c+f)

