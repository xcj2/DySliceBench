from collections import Counter,defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
d = inpl()
m = inp()
t = inpl()
cntd = Counter(d)
cntt = Counter(t)
for key in cntt:
    if cntt[key] > cntd[key]:
        print('NO')
        break
else:
    print('YES')