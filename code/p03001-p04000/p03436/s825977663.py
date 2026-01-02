H, W = (int(i) for i in input().split())
S = []
for i in range(H):
	row = input()
	S.append([(0 if row[j]=="." else 1) for j in range(W)])

D = [[10000 for j in range(W)] for i in range(H)]
R = [[False for j in range(W)] for i in range(H)]

N_black = 0
for i in range(H):
	for j in range(W):
		if S[i][j] == 1:
			D[i][j] = -1
			R[i][j] = True
			N_black += 1

def update(i0, j0, i1, j1):
	global D
	center = D[i0][j0]
	adj = D[i1][j1]
	r = R[i1][j1]
	if adj != -1 and r == False and center + 1 < adj:
		D[i1][j1] = center + 1


def check_around(i ,j):
	# UP
	if i != 0:
		update(i, j, i-1, j)
	# LEFT
	if j != 0:
		update(i, j, i, j-1)
	# DOWN
	if i != H-1:
		update(i, j, i+1, j)
	# RIGHT
	if j != W-1:
		update(i, j, i, j+1)

def minimum_point():
	global H, W
	m = 10001
	ni = 0
	nj = 0
	for i in range(H):
		for j in range(W):
			d = D[i][j]
			if d != -1 and R[i][j] == False and d < m:
				m = d
				ni = i
				nj = j
	return (ni, nj)


D[0][0] = 1
R[0][0] = True

pi = 0
pj = 0

for idx in range(W*H):
	check_around(pi, pj)
	pi, pj = minimum_point()
	R[pi][pj] = True

if D[H-1][W-1] == 10000:
	print(-1)
else:
	print(W*H-D[H-1][W-1]-N_black)