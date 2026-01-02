from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())


N,M = inpl()
lines = defaultdict(set)

for _ in range(M):
    u,v = inpl()
    u -= 1
    v -= 1
    lines[u].add(v+N)
    lines[u+N].add(v+2*N)
    lines[u+2*N].add(v)

S,T = inpl()
S -= 1
T -= 1

def search (s,w_0): #s->t
	global weight
	global q

	for t in list(lines[s]):
		w = w_0 + 1
		if weight[t] > w:
			heapq.heappush(q, [w,t])
			weight[t] = w

# Start, S
weight = [INF]*(N*3)
weight[S] = 0
q = [[0,S]]
heapq.heapify(q)
while q:
	w,n = heapq.heappop(q)
	search(n,w)

ans = weight[T]

if ans == INF:
    print(-1)
else:
    print(ans//3)
