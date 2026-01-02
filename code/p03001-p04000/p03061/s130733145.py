def gcd(x,y):
	if x < y:
		x, y = y, x
	while(y):
		x, y = y, x%y
	return x

def gcds(t,X,V):
	if X[t] > V[t]:
		x, y = X[t], V[t]
	else:
		x, y = V[t], X[t]
	while(y>0):
		x, y = y, x%y
		V[t+1] = x

def gcde(t,X,V):
	if X[t] > V[t+1]:
		x, y = X[t], V[t+1]
	else:
		x, y = V[t+1], X[t]
	while(y>0):
		x, y = y, x%y
		V[t] = x

def main():
	N = int(input())
	A = list(map(int,input().split()))
	ans = 1
	S = [A[0]]*(N+1)
	E = [A[N-1]]*(N+1)
	for t in range(N):
		gcds(t, A, S)
		gcde(N-t-1, A, E)
	ans = max(ans, E[1])
	ans = max(ans, S[N-1])
	for t in range(1,N-1):
		ans = max(ans, gcd(S[t], E[t+1]))
	print(ans)

main()