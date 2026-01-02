from collections import Counter
from math import sqrt

#f_listとf_r_listの要素数は状況に応じて変えよう

MOD = (10 ** 9) + 7

list_size = 3 * (10 ** 5)

f_list = [1] * list_size
f_r_list = [1] * list_size

for i in range(list_size - 1):
	f_list[i + 1] = int((f_list[i] * (i + 2)) % MOD)

def power(n, x):
	if x == 1:
		return n
	elif x % 2 == 0:
		return power(int((n * n) % MOD), int(x / 2))
	else:
		return int((n * power(n, x - 1)) % MOD)

f_r_list[-1] = power(f_list[-1], MOD - 2)

for i in range(2, list_size + 1):
	f_r_list[-i] = int((f_r_list[-i + 1] * (list_size + 2 - i)) % MOD)

def comb(n, r):
	if n < r:
		return 0
	elif n == 0 or r == 0 or n == r:
		return 1
	else:
		return (((f_list[n - 1] * f_r_list[n - r - 1]) % MOD) * f_r_list[r - 1]) % MOD 

def is_prime(i):
	if i == 1:
		return False
	for j in range(2, int(sqrt(i)) + 1):
		if i % j == 0:
			return False
	return True

n, m = map(int, input().split())
prime_factor = Counter()

for i in range(2, int(sqrt(m)) + 1):
	if m % i == 0:
		prime_factor[i] += 1
		m = m // i
		while m % i == 0:
			prime_factor[i] += 1
			m = m // i
	if is_prime(m):
		prime_factor[m] += 1
		break

ans = 1
for i in prime_factor.values():
	ans *= comb(n + i - 1, i)
	ans %= MOD
print(ans)

