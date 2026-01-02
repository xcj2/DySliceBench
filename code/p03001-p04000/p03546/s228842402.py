from collections import defaultdict
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, input().split()))
def inpl_s(): return list(input().split())

H,W = inpl()

lines = defaultdict(set)

for i in range(10):
	li = inpl()
	for j,c in enumerate(li):
		lines[j].add((i,c))

def search (s,w_0): #s->t
	global weight
	global q
	for line in list(lines[s]):
		t = line[0]
		w = w_0 + line[1]
		if weight[t] > w:
			heapq.heappush(q, [w,t])
			weight[t] = w

s = 1
weight = [INF]*10
weight[s] = 0
q = [[0,s]]
heapq.heapify(q)
while q:
	w,n = heapq.heappop(q)
	search(n,w)

ans = 0
for i in range(H):
	li = inpl()
	for l in li:
		if l == -1:
			continue
		else:
			ans += weight[l]

print(ans)
