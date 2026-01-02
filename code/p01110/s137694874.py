import sys
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def LIST(): return list(map(int, input().split()))
def MAP(): return map(int, input().split())

def remove_left(M, c):
	for i in range(len(M)):
		M[i] = M[i][c:]
	return M

def remove_bottom(M, c):
	M = M[:len(M)-c]
	return M

def reverse_tate(M):
	for i in range(len(M)//2):
		for j in range(len(M[0])):
			M[i][j], M[-1-i][j] = M[-1-i][j], M[i][j]

	return M
def reverse_yoko(M):
	for i in range(len(M)):
		M[i] = M[i][::-1]
	return M


def turn_left(M, c):
	if c > len(M[0])/2:
		M = reverse_yoko(M)
		c = len(M[0]) - c
	for i in range(len(M)):
		for j in range(c):
			M[i][c+j] += M[i][c-1-j]
	M = remove_left(M, c)
	return M

def turn_bottom(M, c):
	if c > len(M)/2:
		M = reverse_tate(M)
		c = len(M) - c
	for i in range(len(M[0])):
		for j in range(c):
			M[len(M)-c-1-j][i] += M[len(M)-c+j][i]
	M = remove_bottom(M, c)
	return M

ans = []
while 1:
	n, m, t, p = MAP()
	if (n, m, t, p) == (0, 0, 0, 0):
		break

	dc = [LIST() for _ in range(t)]
	xy = [LIST() for _ in range(p)]

	M = [[1]*n for _ in range(m)]
	for d, c in dc:
		if d == 1:  # 左->右
			M = turn_left(M, c)
		else:  # 下->上
			M = turn_bottom(M, c)

	for x, y in xy:
		ans.append(M[-1-y][0+x])

for i in ans:
	print(i)
	
