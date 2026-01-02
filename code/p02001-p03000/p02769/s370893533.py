mod = 10**9 + 7
max_N = 2 * 10**5

def power(b, e):
	if e == 0: return 1

	half = power(b, e // 2)

	if e % 2 == 0:
		return (half * half) % mod
	else:
		return (((half * half) % mod) * b) % mod

def mod_inv(n):
	return power(n, mod - 2)

fac = [1] * (max_N + 1)
for i in range(1, max_N + 1):
	fac[i] = (i * fac[i - 1]) % mod

fac_inv = [1] * (max_N + 1)
fac_inv[max_N] = mod_inv(fac[max_N])
for i in range(max_N - 1, -1, -1):
	fac_inv[i] = (fac_inv[i + 1] * (i + 1)) % mod

def choose(n, k):
	return (((fac[n] * fac_inv[k]) % mod) * fac_inv[n - k]) % mod


if __name__ == "__main__":
	line = input().split(" ")
	N, K = int(line[0]), int(line[1])
	K = min(K, N - 1)

	ans = 0
	for i in range(K + 1):
		ans = (ans + (choose(N, i) * choose(N - i - 1 + i, i)) % mod) % mod

	print(ans)