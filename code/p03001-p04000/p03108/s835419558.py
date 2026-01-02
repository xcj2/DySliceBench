import sys

input = sys.stdin.readline
#木の根を求める
def find(x):
    if par[x] == x:
        return x
    else:
        return find(par[x])

#xとyの属する集合の併合
def unite(x,y):
    x = find(x)
    y = find(y)
    
    if x != y:
        #xとyの属している集合が異なる時
        if rank[x] < rank[y]:
            par[x] = y
            size[y] += size[x]
        else:
            par[y] = x
            size[x] += size[y]
            if rank[x]==rank[y]:
                rank[x] += 1

#xとyが同じ集合に属するかの判定
def same(x,y):
    return find(x) == find(y)

n, m = map(int,input().split())
bridge = [list(map(lambda x:x-1,list(map(int,input().split())))) for i in range(m)]
par = [i for i in range(n)]
rank = [0] * n
size = [1] * n
res = []
inc = n*(n-1)//2
res.append(inc)
bridge.reverse()
for pair in bridge:
    if same(pair[0],pair[1]):
        unite(pair[0],pair[1])
        res.append(inc)
    else:
        inc -= (size[find(pair[0])] * size[find(pair[1])])
        res.append(inc)
        unite(pair[0],pair[1])

res.reverse()
for ans in res[1:]:
    print(ans)