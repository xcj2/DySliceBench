from collections import defaultdict
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
AtoZ = [chr(i) for i in range(65,65+26)]
atoz = [chr(i) for i in range(97,97+26)]

def inpl(): return list(map(int, input().split()))
def inpl_s(): return list(input().split())


N,M,R = inpl()
rr = inpl()

weight = [[INF for i in range(N)] for j in range(R)]
for r in range(R):
	weight[r][rr[r]-1] = 0

lines = defaultdict(set)
for i in range(M):
	a,b,c = inpl()
	a -= 1
	b -= 1
	lines[a].add((b,c))
	lines[b].add((a,c))

def search (s,w_0,r):
	global weight
	global q
	for line in list(lines[s]):
		t = line[0]
		w = w_0 + line[1]
		if weight[r][t] > w:
			heapq.heappush(q, [w,t])
			weight[r][t] = w

for r in range(R):
	q = [ [0, rr[r]-1] ]
	heapq.heapify(q)
	while q:
		w_0,s = heapq.heappop(q)
		search(s,w_0,r)

ans = INF
for li in list(itertools.permutations(range(R))):
	tmp = 0
	for i in range(R-1):
		s = li[i]
		t = li[i+1]
		tmp += weight[s][rr[t]-1]
	ans = min(ans,tmp)

print(ans)