MOD = 10 ** 9 + 7

def modPow(a, x, p):
	res = 1
	while x > 0:
		if x % 2 != 0:
			res = res * a % p
		a = a * a % p
		x = x // 2
	return res
 
def modInverse(a, p):
	return modPow(a, p - 2, p)
 
def modBinomial(n, k, p):
	numerator = 1
	for i in range(k):
		numerator = (numerator * (n - i)) % p
	denominator = 1
	for i in range(1, k + 1):
		denominator = (denominator * i) % p
	return (numerator * modInverse(denominator, p)) % p


if __name__ == "__main__":
	X, Y = map(int, input().split())
	if (X + Y) % 3 != 0 or Y > 2 * X or Y < X / 2.:
		print("0")
	else:
		n = (X + Y) // 3
		k = Y - n
		print(modBinomial(n, k, MOD))