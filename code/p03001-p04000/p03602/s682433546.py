#設定
import sys
input = sys.stdin.buffer.readline

#ライブラリインポート
from collections import defaultdict
import copy

INF = float("inf")

#入力受け取り
def getlist():
	return list(map(int, input().split()))

def build(d, n):
	cost = 0
	for k in range(n):
		for i in range(n):
			for j in range(n):
				if d[i][j] == d[i][k] + d[k][j] and k != i and k != j:
					d[i][j] = INF
				
	return d

def judge(d, n):
	for k in range(n):
		for i in range(n):
			for j in range(n):
				d[i][j] = min(d[i][j],d[i][k] + d[k][j])
	return d

#処理内容
def main():
	#受け取り
	N = int(input())
	d = []
	for i in range(N):
		g = getlist()
		d.append(g)

	#ワーシャルフロイド判定
	d2 = copy.deepcopy(d)
	d2 = judge(d2, N)

	if d != d2:
		print(-1)
	else:
		#構築
		X = build(d2, N)
		ans = 0
		for i in range(N):
			for j in range(N):
				if d2[i][j] != INF:
					ans += d2[i][j]
		print(ans // 2)


if __name__ == '__main__':
	main()