n,m = map(int, input().split())

par = [i for i in range(n)]
rank = [0]*n

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    if rank[x]<rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

def same(x,y):
    return find(x) == find(y)

a = []
b = []

for i in range(m):
    x,y = map(int, input().split())
    a.append(x-1)
    b.append(y-1)

ans = 0
for i in range(m):
    par = [k for k in range(n)]
    rank = [0]*n
    # i番目の2頂点以外を連結
    for j in range(m):
        if i != j:
            unite(a[j],b[j])
            
    
    # 全ての点が連結してるか確認
    if not same(a[i],b[i]):
        ans+=1
  

print(ans)



