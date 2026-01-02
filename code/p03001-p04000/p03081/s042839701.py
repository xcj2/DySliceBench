N, Q = map(int, input().split())
s = input()

def conv(t, d):
	return t, (1 if d == 'R' else -1)

*queries, = (conv(*input().split()) for i in range(Q))

def simulate(i, left=True):
	if i < 0:
		return left
	elif N <= i:
		return not left
	
	for t, d in queries:
		if t == s[i]:
			i += d
		if i < 0:
			return left
		elif N <= i:
			return not left
	return False

def search(ok=0, ng=N+1, left=True):
	while abs(ok - ng) > 1:
		mid = (ok + ng) // 2
		if simulate(mid, left):
			ok = mid
		else:
			ng = mid
	return ok

print(N - (1 + search(-1, N, True) + (N - search(N, -1, False))))
