maxn = 100000

n , q = map(int, input().split())

par = [0] * n
rank = [0] * n

#初期化
for i in range(n):
    par[i] = i
    rank[i] = 0

#判定(一番上野根を求める)
def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
    
#結合
def unite(x , y):
    rx = find(x)
    ry = find(y)
    
    if rx == ry:
        return
    
    if rank[rx] < rank[ry]:
        par[rx] = ry
    elif rank[rx] > rank[ry]:
        par[ry] = rx
    else:
        par[ry] = x
        rank[rx] += 1      

def same(x,y):
    return find(x) == find(y)

for i in range(q):
    p,a,b = map(int, input().split())
    if p == 0:
        unite(a,b)
    if p == 1:
        print(1 if same(a,b) else 0)
