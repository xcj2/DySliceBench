#ライブラリインポート
from collections import defaultdict

#入力受け取り
def getlist():
	return list(map(int, input().split()))

p = 10 ** 9 + 7
p2 = 10 ** 9 + 9
q = 1007
q2 = 2009

def rollingHash(N, M, A, ans):
	mul1 = 1
	mul2 = 1
	for i in range(M):
		mul1 = (mul1 * q) % p
		mul2 = (mul2 * q2) % p2

	Droll1 = defaultdict(lambda:-1)
	Droll2 = defaultdict(lambda:-1)
	val1 = 0
	val2 = 0
	for i in range(M):
		val1 = val1 * q + A[i]
		val1 %= p
		val2 = val2 * q2 + A[i]
		val2 %= p2

	Droll1[val1] = 0
	Droll2[val2] = 0
	rolling_Hash1 = [None] * (N - M + 1)
	rolling_Hash1[0] = val1
	rolling_Hash2 = [None] * (N - M + 1)
	rolling_Hash2[0] = val2

	for i in range(N - M):
		val1 = (val1 * q - A[i] * mul1 + A[i + M]) % p
		val2 = (val2 * q2 - A[i] * mul2 + A[i + M]) % p2
		rolling_Hash1[i + 1] = val1
		rolling_Hash2[i + 1] = val2

		if Droll1[val1] == -1:
			Droll1[val1] = i + 1
		else:
			if rolling_Hash1[i + 1] == rolling_Hash1[Droll1[val1]] and rolling_Hash2[i + 1] == rolling_Hash2[Droll1[val1]] and i + 1 - Droll1[val1] >= M:
				return M

	return ans

#処理内容
def main():
	N = int(input())
	S = list(input())
	for i in range(N):
		S[i] = ord(S[i]) - 97

	ans = 0
	for i in range(1, int(N // 2) + 1):
		ans = rollingHash(N, i, S, ans)

	print(ans)



if __name__ == '__main__':
	main()