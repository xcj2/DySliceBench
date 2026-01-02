#Union Find

#xの根を求める
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
#xとyの属する集合の併合
def unite(x,y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return False
    else:
        #sizeの大きいほうがx
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y]
        par[y] = x
        return True

#xとyが同じ集合に属するかの判定
def same(x,y):
    return find(x) == find(y)

#xが属する集合の個数
def size(x):
    return -par[find(x)]


n = int(input())

edge = [[] for _ in [0]*n]
for i in range(n):
	s = input()
	for j in range(n):
		if s[j] == '1':
			edge[i].append(j)


res = -1
for start in range(n):
	par = [-1]*n
	used = [False]*n
	used[start] = True

	tank = set()
	new = {start}
	judge = True

	while len(new) != 0 and judge:
		tank = set()
		for e in new:
			for go in edge[e]:
				if not used[go]:
					if same(e,go):
						judge = False
					else:
						tank.add(go)
		for e in new:
			used[e] = True
		if len(tank) >= 1:
			qqq = list(tank)[0]
			for e in tank:
				unite(e,qqq)
		new = tank

	if judge:
		cnt = 0
		for e in par:
			if e < 0:
				cnt += 1
		res = max(cnt,res)
print(res)






