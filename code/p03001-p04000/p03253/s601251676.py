# 素因数分解
def prime_decomposition(n):
	i = 2
	table = []
	while i * i <= n:
		while n % i == 0:
			n //= i
			table.append(i)
		i += 1
	if n > 1:
		table.append(n)
	return table

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

# mを法とするaの乗法的逆元
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# nCr mod m
def combination(n, r, mod=10**9+7):
	r = min(r, n-r)
	res = 1
	for i in range(r):
		res = res * (n - i) * modinv(i+1, mod) % mod
	return res

# nHr mod m
def H(n, r, mod=10**9+7):
	return combination(n+r-1, r, mod)

from collections import defaultdict
N, M = map(int, input().split())
prime_table = prime_decomposition(M)
dic = defaultdict(int) #指数のリスト
for p in prime_table:
    dic[p] += 1

ans=1
for p, b in dic.items():
	ans *= H(N, b, mod=10**9+7)
print(ans%(10**9+7))