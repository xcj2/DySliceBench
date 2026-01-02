#木の根を求める
def find(x,par):
    if par[x] == x:
        return x
    else:
        return find(par[x],par)

#xとyの属する集合の併合
def unite(x,y,par,rank):
    x = find(x,par)
    y = find(y,par)
    
    if x != y:
        #xとyの属している集合が異なる時
        if rank[x] < rank[y]:
            par[x] = y
        else:
            par[y] = x
            if rank[x]==rank[y]:
                rank[x] += 1

#xとyが同じ集合に属するかの判定
def same(x,y,par):
    return find(x,par) == find(y,par)
    
n, m = map(int, input().split())
a, b = [], []
ans = 0
for i in range(m):
    ta, tb = map(int,input().split())
    a.append(ta-1)
    b.append(tb-1)
    
for i in range(m):
    par = []
    rank = []
    diff = set()
    for j in range(n): # 初期化
        par.append(j)
        rank.append(0)
    for j in range(m):
        if j == i:
            continue
        else:
            unite(a[j],b[j],par,rank)
    for j in range(n):
        diff.add(find(j,par))
    if len(diff) == 1:
        continue
    else:
        ans += 1
print(ans)