import sys; input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**7)
from collections import defaultdict
mod = 998244353; INF = float("inf")

def getlist():
	return list(map(int, input().split()))

def inverse(N, mod):
	return (pow(N, mod - 2, mod))

def main():
	N, K = getlist()
	DP = [0] * (2 * N + 1)
	DP2 = [0] * (2 * N + 1)
	DP[0] = 1
	LR = []
	for i in range(K):
		L, R = getlist()
		LR.append([L, R])

	for i in range(N):
		DP[i] += DP2[i]
		DP[i] %= mod
		for l, r in LR:
			DP2[i + l] += DP[i]
			DP2[i + l] %= mod
			DP2[i + r + 1] -= DP[i]
			DP2[i + r + 1] %= mod
		DP2[i + 1] += DP2[i]
		DP2[i + 1] %= mod

	ans = DP[N - 1]
	print(ans % mod)

if __name__ == '__main__':
	main()