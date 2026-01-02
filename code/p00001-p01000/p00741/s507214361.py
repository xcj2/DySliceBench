import sys

sys.setrecursionlimit(10**6)


def is_in_map(x, y, w, h):
	return 0 <= x < w and 0 <= y < h


def dfs(x, y, lct):
	lct[y][x] = 0
	w = len(lct[0])
	h = len(lct)

	for i in range(-1, 2):
		for j in range(-1, 2):
			nx = x + i
			ny = y + j
			if not is_in_map(nx, ny, w, h):
				continue
			if lct[ny][nx] == 0:
				continue
			dfs(nx, ny, lct)

def resolve():
	while True:
		w, h = map(int, input().split())

		if w == 0 and h == 0:
			break

		ans = 0
		lct = []

		for _ in range(h):
			lct.append(list(map(int, input().split())))
		for i in range(h):
			for j in range(w):
				if lct[i][j] == 0:
					continue
				dfs(j, i, lct)
				ans += 1
		print(ans)

resolve()

