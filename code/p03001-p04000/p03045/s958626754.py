# union-findかな
# 蟻本によればunion-findは分割できないっぽいので、ちょっと違う? 
# 時刻を巻き戻して、橋なしから橋を建設することにすれば扱える

# 橋が崩落してA+B　がAとBに分かれたら、不便度はA*B増加する

n,m = map(int, input().split())

def find_root(x):
	if par[x] == x:
		return x
	else:
		par[x] = find_root(par[x])
		return par[x]

def unite(x, y):
	x = find_root(x)
	y = find_root(y)
	if(x == y):
		return 0

	if rank[x] < rank[y]:
		par[x] = y

		temp = size[x] * size[y]
		size[y] = size[x] + size[y]
	else:
		par[y] = x
		if (rank[x] == rank[y]):
			rank[x] += 11

		temp = size[x] * size[y]
		size[x] = size[x] + size[y]
	return temp

def is_same(x,y):
	return find_root(x) == find_root(y)

# par = [0]*n
par = list(range(n))
rank = [0]*n
size = [1]*n

edges = [list(map(int, input().split()))[0:2] for _ in range(m)]
edges = [[b[0]-1, b[1]-1] for b in edges] #1-idx -> 0-idx

for b in range(m):
	unite(edges[b][0] , edges[b][1])

# print(par)
# print(len(set(par)))

arr = [0] * n
for i in range(n):
	arr[i] = find_root(i)

print(len(set(arr)))
