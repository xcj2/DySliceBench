n,m = map(int,input().split())
p = list(map(int,input().split()))
for i in range(n):
    p[i]-=1
####################################
#Union Find
par = [] #親
rank = [] #木の深さ

#初期化
for i in range(n):
    #par[i]:i rank[i]:0
    par.append(i)
    rank.append(0)

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



#######################################
for i in range(m):
    x,y = map(int,input().split())
    x -= 1
    y -=1
    unite(x,y,par,rank)

a = [[] for i in range(n)]
b = [[] for i in range(n)]
for i in range(n):
    k = find(i,par)
    a[k].append(i)
    b[k].append(p[i])

res = 0
for i in range(n):
    if len(a[i])!= 0 and len(b[i])!=0:
        res += len(set(a[i])&set(b[i]))
print(res)