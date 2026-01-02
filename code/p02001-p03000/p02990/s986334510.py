MOD = 10**9 + 7
N,K = map(int,input().split())
def powmod(a, n):
	ans = 1
	while n > 0:
		if n % 2 == 0:
			a = (a * a) % MOD
		else:
			ans = (ans * a) % MOD
			a = (a * a) % MOD
		n = n // 2
	return ans

def fact(n):
	ans = 1
	for i in range(2, n+1):
		ans = (ans * i) % MOD
	return ans
def combination(n,k):
	bunbo = fact(n)
	bunshi = (fact(k) * fact(n-k)) % MOD
	return bunbo * powmod(bunshi, MOD-2)

print(N-K+1)
for i in range(2,K+1):
	ans = 0
	if N-K >= i-1:
		B = combination(K-1, i-1)
		ans = (ans + (combination(N-K+1, i) * B) % MOD) % MOD
	print(ans)