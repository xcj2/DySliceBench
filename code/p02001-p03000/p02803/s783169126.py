#ライブラリインポート
import queue

#入力受け取り
def getlist():
	return list(map(int, input().split()))

INF = float("inf")

def BFS(H, W, L, start):
	dist = [[INF for i in range(W)] for j in range(H)]
	sy, sx = start
	dist[sy][sx] = 0
	Q = queue.Queue()
	Q.put([sy, sx])
	while not Q.empty():
		y, x = Q.get()
		if y - 1 >= 0:
			if L[y - 1][x] == "." and dist[y - 1][x] > dist[y][x] + 1:
				dist[y - 1][x] = dist[y][x] + 1
				Q.put([y - 1, x])
		if y + 1 <= H - 1:
			if L[y + 1][x] == "." and dist[y + 1][x] > dist[y][x] + 1:
				dist[y + 1][x] = dist[y][x] + 1
				Q.put([y + 1, x])
		if x - 1 >= 0:
			if L[y][x - 1] == "." and dist[y][x - 1] > dist[y][x] + 1:
				dist[y][x - 1] = dist[y][x] + 1
				Q.put([y, x - 1])
		if x + 1 <= W - 1:
			if L[y][x + 1] == "." and dist[y][x + 1] > dist[y][x] + 1:
				dist[y][x + 1] = dist[y][x] + 1
				Q.put([y, x + 1])

	return dist

#処理内容
def main():
	H, W = getlist()
	L = []
	for i in range(H):
		l = list(input())
		L.append(l)

	ans = 0
	for i in range(H):
		for j in range(W):
			if L[i][j] == ".":
				BF = BFS(H, W, L, [i, j])
				for p in range(H):
					for q in range(W):
						if BF[p][q] != INF:
							ans = max(ans, BF[p][q])

	print(ans)


if __name__ == '__main__':
	main()