from itertools import product

INF = 1000000007

def mat2_mul(X, Y):
	z = [[0, 0], [0, 0]]
	for (i, j, k) in product(range(2), range(2), range(2)):
		z[i][j] += X[i][k] * Y[k][j]
	return z

def mat2_pow(X, n):
	if n == 0:
		return [[1, 0], [0, 1]]
	elif n % 2:
		return mat2_mul(X, mat2_pow(X, n - 1))
	else:
		half_pow = mat2_pow(X, n / 2)
		return mat2_mul(half_pow, half_pow)

def fib(n):
	if n == 0:
		return 0
	else:
		f = [[0, 1], [1, 1]]
	return mat2_pow(f, n - 1)[1][1]


N, M = map(int, input().split())
a = [int(input()) for _ in range(M)]
ans, start = 1, 0

for k in a:
	ans *= fib(k - start)
	ans %= INF
	start = k + 1

ans *= fib(N - start + 1)
print(ans % INF)
