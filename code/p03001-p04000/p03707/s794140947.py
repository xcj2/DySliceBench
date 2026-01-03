import sys
def input():
	return sys.stdin.readline()[:-1]

n, m, q = map(int, input().split())
s = ["0"*(m+1)] + ["0" + input() for _ in range(n)]

block = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
	for j in range(1, m+1):
		block[i][j] = block[i][j-1] + block[i-1][j] - block[i-1][j-1] + int(s[i][j])

def block_num(x1, y1, x2, y2):
	return block[x2][y2] - block[x1-1][y2] - block[x2][y1-1] + block[x1-1][y1-1]

edge_h = [[0 for _ in range(m)] for _ in range(n+1)]
edge_v = [[0 for _ in range(m+1)] for _ in range(n)]

for i in range(1, n+1):
	for j in range(1, m):
		edge_h[i][j] = edge_h[i][j-1] + edge_h[i-1][j] - edge_h[i-1][j-1] + (int(s[i][j]) + int(s[i][j+1]) == 2)

for i in range(1, n):
	for j in range(1, m+1):
		edge_v[i][j] = edge_v[i][j-1] + edge_v[i-1][j] - edge_v[i-1][j-1] + (int(s[i][j]) + int(s[i+1][j]) == 2)

def edge_num(x1, y1, x2, y2):
	h = edge_h[x2][y2-1] - edge_h[x1-1][y2-1] - edge_h[x2][y1-1] + edge_h[x1-1][y1-1]
	v = edge_v[x2-1][y2] - edge_v[x1-1][y2] - edge_v[x2-1][y1-1] + edge_v[x1-1][y1-1]
	return h+v

for _ in range(q):
	x1, y1, x2, y2 = map(int, input().split())
	b = block_num(x1, y1, x2, y2)
	e = edge_num(x1, y1, x2, y2)
	print(b-e)