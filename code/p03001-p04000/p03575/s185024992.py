N, M = map(int, input().split())
 
lines = []
for _ in range(M):
	lines.append(list(map(lambda x: int(x) - 1, input().split())))
 
def root(x):
	if par[x] == x:
		return x
	
	par[x] = root(par[x])
	return par[x]
 
def unite(x, y):
	rx = root(x)
	ry = root(y)
	if rx != ry:
		par[rx] = ry
 
def same(x, y):
	rx = root(x)
	ry = root(y)
	return rx == ry
 
 
ans = 0
 
for i in range(M):
	par = [x for x in range(N)]
	
	for j in range(M):
		if i != j:
			unite(lines[j][0], lines[j][1])
	
	flag = True
	for j in range(1, N):
		if not same(0, j):
			flag = False
	if not flag:
		ans += 1
 
print(ans)