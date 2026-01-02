#設定
import sys
input = sys.stdin.buffer.readline

#ライブラリインポート
from collections import defaultdict

#入力受け取り
def getlist():
	return list(map(int, input().split()))

#処理内容
def main():
	N, X = getlist()
	B = [0] * 51
	P = [0] * 51
	Size = [0] * 51
	P[0] = 1
	for i in range(50):
		B[i + 1] = 2 * B[i] + 2
		P[i + 1] = 2 * P[i] + 1
	for i in range(51):
		Size[i] = B[i] + P[i]

	def solve(N, X):
		if N == 0:
			return 1
		elif X == 1:
			return 0
		elif X <= 1 + Size[N - 1]:
			return solve(N - 1, X - 1)
		elif X == 2 + Size[N - 1]:
			return P[N - 1] + 1
		elif 2 + Size[N - 1] < X and X <= 2 + 2 * Size[N - 1]:
			return (P[N - 1] + 1 + solve(N - 1, X - 2 - Size[N - 1]))
		else:
			return 2 * P[N - 1] + 1

	ans = solve(N, X)
	print(ans)

if __name__ == '__main__':
	main()