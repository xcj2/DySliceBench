from collections import deque

def reachable(es, source):
	ret = {source}
	Q = [source]
	while Q:
		cur = Q.pop()
		for nxt in es[cur]:
			if nxt not in ret:
				Q.append(nxt)
				ret.add(nxt)
	return ret

def SPFA(G:list, source=0):
	V = len(G)
	d = [float("inf")]*V
	inQ = [False]*V
	cnt = [0]*V
	d[source] = 0
	cnt[source] = 1
	Q = deque([source])
	while Q:
		f = Q.popleft()
		inQ[f] = False
		for t,c in G[f]:
			dist = d[f] + c
			if dist < d[t]:
				d[t] = dist
				if not inQ[t]:
					Q.append(t)
					inQ[t] = True
					cnt[t] += 1
					front = Q.popleft()
					if d[front] > dist:
						Q.append(front)
					else:
						Q.appendleft(front)
				if cnt[t] > V:
					#negative cycle
					return None
	return d[-1]
	
def main():
	N,M,P,*L=map(int,open(0).read().split())
	fwd = [[] for _ in range(N)]
	bwd = [[] for _ in range(N)]
	G = [[] for _ in range(N)]
	for a,b in zip(L[::3],L[1::3]):
		fwd[a-1].append(b-1)
		bwd[b-1].append(a-1)
	judge = reachable(fwd,0) & reachable(bwd,N-1)
	for a,b,c in zip(*[iter(L)]*3):
		if a-1 in judge and b-1 in judge:
			G[a-1].append((b-1,P-c))
	ans = SPFA(G)
	if ans==None:
		print(-1)
	else:
		print(max(0,-ans))

if __name__=="__main__":
	main()