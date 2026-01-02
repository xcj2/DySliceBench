#設定
import sys
input = sys.stdin.buffer.readline

#ライブラリインポート
from collections import defaultdict

INF = float("inf")

def getlist():
	return list(map(int, input().split()))

def warshall_floyd(d, n):
	for k in range(n):
		for i in range(n):
			for j in range(n):
				d[i][j] = min(d[i][j],d[i][k] + d[k][j])
	return d


#処理内容
def main():
	N, M, L = getlist()
	d = [[float("inf") for i in range(N)] for i in range(N)]
	for i in range(M):
		a, b, w = getlist()
		d[a - 1][b - 1] = w
		d[b - 1][a - 1] = w

	for i in range(N):
		d[i][i] = 0

	d = warshall_floyd(d, N)
	d2 = [[float("inf") for i in range(N)] for i in range(N)]
	for i in range(N):
		for j in range(N):
			if d[i][j] <= L:
				d2[i][j] = 1
	for i in range(N):
		d2[i][i] = 0

	d2 = warshall_floyd(d2, N)

	Q = int(input())
	for i in range(Q):
		s, t = getlist()
		if d2[s - 1][t - 1] == INF:
			print(-1)
		else:
			print(d2[s - 1][t - 1] - 1)



if __name__ == '__main__':
	main()