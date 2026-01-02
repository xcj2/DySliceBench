import sys; input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**7)
from collections import defaultdict
mod = 10 ** 9 + 7; INF = float("inf")

def getlist():
	return list(map(int, input().split()))

def inverse(N, mod):
	return (pow(N, mod - 2, mod))

def main():
	N, X, M = getlist()
	if N <= 10 ** 6:
		cnt = 0
		A = X
		cnt += A
		for i in range(N - 1):
			A = (A ** 2) % M
			cnt += A

		print(cnt)
		return

	A = X
	D = defaultdict(int)
	L = [0] * (2 * 10 ** 5)
	L[1] = A
	D[A] = 1

	for i in range(2, N + 2):
		A = (A ** 2) % M
		if D[A] != 0:
			start = D[A]
			loop = i - D[A]
			break
		D[A] = i
		L[i] = A

	ans = 0
	for i in range(start, start + loop):
		ans += L[i]

	p = int((N - start + 1) // loop)
	ans *= p

	for i in range(1, start):
		ans += L[i]

	q = N - loop * p - start + 1
	for i in range(start, start + q):
		ans += L[i]

	print(ans)


if __name__ == '__main__':
	main()