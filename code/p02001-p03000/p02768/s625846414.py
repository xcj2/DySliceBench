mod = 10**9 + 7

def power(b, e):
	if e == 0: return 1

	half = power(b, e // 2)

	if e % 2 == 0:
		return (half * half) % mod
	else:
		return (((half * half) % mod) * b) % mod

def mod_inv(n):
	return power(n, mod - 2)

def choose(n, a):
	num = 1
	den = 1
	for i in range(1, a + 1):
		num = (num * (n - i + 1)) % mod
		den = (den * i) % mod

	# print("inv:", mod_inv(den))
	# print(num, den)
	return (num * mod_inv(den)) % mod


if __name__ == "__main__":
	line = input().split(" ")
	n, a, b = int(line[0]), int(line[1]), int(line[2])

	# print(power(2, n))
	# print("nca", choose(n, a))
	# print("ncb", choose(n, b))
	ans = (power(2, n) - choose(n, a) - choose(n, b) - 1 + 2* mod) % mod 

	print(ans)