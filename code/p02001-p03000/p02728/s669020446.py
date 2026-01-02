#ABC160F

import sys
sys.setrecursionlimit(10**7)

def input():
	return sys.stdin.buffer.readline()[:-1]

MOD = 10**9+7
n = int(input())
con = [[] for _ in range(n)]
for _ in range(n-1):
	a, b = map(int, input().split())
	con[a-1].append(b-1)
	con[b-1].append(a-1)
stair = [1] #階乗MOD
stairr = [1] #階乗逆数MOD
for i in range(n):
	stair.append((stair[i] * (i+1)) % MOD)
	stairr.append(pow((stair[i] * (i+1)) % MOD, MOD-2, MOD))
cnt = [1 for _ in range(n)]
des_size = [1 for _ in range(n)]
des_case = [1 for _ in range(n)]
def dfs1(v, u):
	totalsize = 1 #v自身も含んだsizeであることに注意
	totalcase = 1
	for w in con[v]:
		if w == u:
			continue
		dfs1(w, v)
		totalsize += des_size[w]
		totalcase = (totalcase * des_case[w] * stairr[des_size[w]]) % MOD
	totalcase = (totalcase * stair[totalsize-1]) % MOD
	des_size[v] = totalsize
	des_case[v] = totalcase
	#print(v, u, totalsize, totalcase)
	#print(des_size)
	#print(des_case)
	return

dfs1(0, -1)
#print(des_size) 
#print(des_case)
asc_size = [1 for _ in range(n)]
asc_case = [1 for _ in range(n)]
def dfs2(v, u):
	if u == -1:
		for w in con[v]:
			if w == u:
				continue 
			dfs2(w, v)
		return
	asc_size[v] = n - des_size[v] + 1
	x0 = des_size[u]
	y0 = des_case[u]
	x1 = des_size[v]
	y1 = des_case[v]
	x2 = asc_size[u]
	y2 = asc_case[u]
	p = (y0 * y2 * stair[x1] * stair[x0+x2-x1-2]) % MOD
	q = (stairr[x0-1] * stairr[x2-1] * pow(y1, MOD-2, MOD)) % MOD
	asc_case[v] = (p*q) % MOD
	#print(v, u, asc_size, asc_case, p, q)
	for w in con[v]:
		if w == u:
			continue 
		dfs2(w, v)
	return
dfs2(0, -1)
#print(asc_size) 
#print(asc_case)

for i in range(n):
	r = stair[des_size[i] + asc_size[i] -2]
	s = (stairr[des_size[i]-1] * stairr[asc_size[i]-1]) % MOD
	t = (des_case[i] * asc_case[i]) % MOD
	print((r * s * t) % MOD)