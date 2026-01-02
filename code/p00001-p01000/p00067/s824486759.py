# AOJ 0067 The Number of Island
# Python3 2018.6.16 bal4u

# UNION-FIND library
MAX = 12*12

id, size = [0]*MAX, [0]*MAX

def init(n):
	for i in range(n): id[i], size[i] = i, 1
	
def root(i):
	while i != id[i]:
		id[i] = id[id[i]]
		i = id[i]
	return i
	
def connected(p, q):
	return root(p) == root(q)
	
def unite(p, q):
	i, j = root(p), root(q)
	if i == j: return
	if size[i] < size[j]:
		id[i] = j
		size[j] += size[i]
	else:
		id[j] = i
		size[i] += size[j]
# UNION-FIND library

arr = [[0 for r in range(12)] for c in range(12)]
dr = [-1, 0, 1, 0]
dc = [ 0, 1, 0,-1]

while True:
	init(12*12)
	for r in range(12): arr[r] = list(map(int, input()))

	for r in range(12):
		for c in range(12):
			if arr[r][c] == 0: continue
			for i in range(4):
				nr, nc = r + dr[i], c + dc[i]
				if nr >= 0 and nr < 12 and nc >= 0 and nc < 12:
					if arr[nr][nc] == 1:
						unite(r*12+c, nr*12+nc)
	
	ans = 0
	for r in range(12):
		for c in range(12):
			if arr[r][c] == 1 and root(r*12+c) == r*12+c: ans += 1

	print(ans)
	try: input()
	except: break
