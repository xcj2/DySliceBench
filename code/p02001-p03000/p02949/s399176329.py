from collections import deque

def reachable(es, source):
	ret = {source}
	Q = deque([source])
	while Q:
		cur = Q.popleft()
		for nxt in es[cur]:
			if nxt not in ret:
				Q.append(nxt)
				ret.add(nxt)
	return ret

def SPFA(G:list, source=0):
	from collections import deque
	V = len(G)
	d = [float("inf")]*V
	inQ = [False]*V
	cnt = [0]*V
	d[source] = 0
	cnt[source] = 1
	Q = deque([source])
	_sum = 0
	_len = 1
	while Q:
		f = Q.popleft()
		inQ[f] = False
		_sum -= d[f]
		_len -= 1
		for t,c in G[f]:
			dist = d[f] + c
			if dist < d[t]:
				d[t] = dist
				if not inQ[t]:
					inQ[t] = True
					cnt[t] += 1
					if dist*_len < _sum:
						Q.appendleft(t)
					else:
						Q.append(t)
					_sum += dist
					_len += 1
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