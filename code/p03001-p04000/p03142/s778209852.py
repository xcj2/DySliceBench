from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())


N,M = inpl()
lines = defaultdict(set)
incnts = [0]*N
for _ in range(N+M-1):
    x,y = inpl()
    x,y = x-1,y-1
    lines[x].add(y)
    incnts[y] += 1

s = incnts.index(0)
ans = [-1]*N
ans[s] = -1

q = queue.Queue()
q.put(s)
while not q.empty():
    s = q.get()
    for t in lines[s]:
        incnts[t] -= 1
        if incnts[t] == 0:
            ans[t] = s
            q.put(t)

for a in ans:
    print(a+1)
