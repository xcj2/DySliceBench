
import sys
def input():
	return sys.stdin.readline().strip()


X, Y = list(map(int, input().split()))

if (X + Y) % 3 != 0 or X > 2*Y or Y > 2*X:
	print(0)
	exit()

times = (X + Y) // 3

times2 = X - times


def fact(n, mod=1000000007):
	ans = 1
	for i in range(n):
		ans *= i + 1
		if mod != 0 and ans >= mod:
			ans = ans % mod
	return ans


def mod_rev(x, mod):

	return pow(x, mod - 2, mod)



def comb(a, b, mod=1000000007):
	"""
	関数mod_rev, fact, powが必要
	"""
	if a < b or b < 0:
		return 0
	if a == b or b == 0:
		return 1
	a_fact = fact(a, mod)
	b_fact = fact(b, mod)
	a_b_fact = fact(a - b, mod)
	if mod != 0:
		return (a_fact * mod_rev(b_fact, mod) * mod_rev(a_b_fact, mod))%mod
	else:
		return a_fact//(b_fact*a_b_fact)

mod = 10**9 + 7

print(comb(times, times2, mod))