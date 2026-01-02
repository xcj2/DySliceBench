from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

N,Q = inpl()

lines = defaultdict(set)
for _ in range(N-1):
    a,b = inpl()
    a,b = a-1,b-1
    lines[a].add(b)

adds = [0]*N
for _ in range(Q):
    p,x = inpl()
    adds[p-1] += x

visited = [False]*N
ans = [0]*N

q = queue.LifoQueue()
q.put([0,0])

while not q.empty():
    x,cnt = q.get()
    cnt += adds[x]
    ans[x] += cnt
    for t in lines[x]:
        q.put([t,cnt])

print(' '.join(map(str,ans)))
