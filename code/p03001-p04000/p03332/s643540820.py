import sys
def input():
	return sys.stdin.readline().strip()

N, A, B, K = list(map(int, input().split()))

mod = 998244353

fact_list = [1]
for i in range(1, N + 1):
	fact_list.append((fact_list[-1]*i) % mod)

def pow(x, y, mod=1000000007):
	pow_list = [x]
	i = 1
	while 2**i <= y:
		a = pow_list[-1]**2
		if mod != 0:
			a = a % mod
		pow_list.append(a)
		i += 1
	ans = 1
	for bit in range(len(pow_list)):
		if (2**bit) & y != 0:
			ans *= pow_list[bit]
			if mod != 0:
				ans = ans % mod
	return ans

def fact(n, mod=1000000007):
	return fact_list[n]
  
rev_list = [1]
for i in range(N):
  rev_list.append(pow(fact(i + 1, mod), mod - 2, mod))

def mod_rev(x, mod):
	"""
	関数powが必要
	"""
	return rev_list[x]


def comb(a, b, mod=1000000007):
	"""
	関数mod_rev, fact, powが必要
	"""
	if a < b or b < 0:
		return 0
	a_fact = fact(a, mod)
	b_fact = fact(b, mod)
	a_b_fact = fact(a - b, mod)
	if mod != 0:
		return (a_fact * mod_rev(b, mod) * mod_rev(a - b, mod))%mod
	else:
		return a_fact//(b_fact*a_b_fact)

ans = 0
for r in range(N + 1):
	rest = K - r * A
	if rest % B == 0 and rest // B >= 0 and rest // B <= N:
		b = rest // B
		ans += comb(N, r, mod)*comb(N, b, mod)
		ans %= mod

print(ans)