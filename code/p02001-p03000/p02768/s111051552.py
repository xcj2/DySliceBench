MOD = 1000000007

n, a, b = map(int, input().split())

# https://tex2e.github.io/blog/crypto/modular-mul-inverse
def xgcd(a, b):
	x0, y0, x1, y1 = 1, 0, 0, 1
	while b != 0:
		q, a, b = a // b, b, a % b
		x0, x1 = x1, x0 - q * x1
		y0, y1 = y1, y0 - q * y1
	return a, x0, y0

# https://tex2e.github.io/blog/crypto/modular-mul-inverse
def modinv(a, m):
	g, x, y = xgcd(a, m)
	if g != 1:
		raise Exception('modular inverse does not exist')
	else:
		return x % m

def combination(n, r):
	ans = 1
	for i in range(n - r + 1, n + 1):
		ans *= i
		ans %= MOD
	for i in range(1, r + 1):
		ans *= modinv(i, MOD)
		ans %= MOD
	return ans

ans = 0
ans += pow(2, n, MOD) - 1
ans += MOD - combination(n, a)
ans += MOD - combination(n, b)
ans %= MOD

print(ans)
