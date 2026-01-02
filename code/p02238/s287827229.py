def dfs_init(color,n,dq):
	for i in range(n):
		color[i] = "White"

def next(u):
	for v in range(list_next[u],n):
		list_next[u] = v+1
		if list_m[u][v]:
			return v


def dfs_visit(u,color,dq,tt):
	tt = tt
	dq.append(u)
	color[u] = "Gray"
	list_d[u] = tt + 1
	tt += 1
	while dq:
		u = dq[-1]
		v = next(u)
		if v != None:
			if color[v] == "White":
				color[v] = "Gray"
				list_d[v] = tt + 1
				tt += 1
				dq.append(v)
		else:
			dq.pop()
			color[u] = "Black"
			list_f[u] = tt + 1
			tt += 1
	return tt

from collections import deque
n = int(input())
list_m = [[0]*n for i in range(n)]
list_next = [0] * n
list_color = [0] * n
list_d = [0]*n
list_f = [0]*n
dq = deque([])

for i in range(n):
	a,b,*args = map(int, input().split())
	for num in args:
		list_m[a-1][num-1] = 1
tt = 0
list_num = [i+1 for i in range(n)]
dfs_init(list_color,n,dq)
for u in range(n):
	if list_color[u] == "White":
		tt = dfs_visit(u,list_color,dq,tt)

for i in range(n):
	print(list_num[i], list_d[i] ,list_f[i])
