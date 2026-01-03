#木の根を求める
def find(x,par):
    if par[x] == x:
        return x
    else:
        return find(par[x],par)

#xとyの属する集合の併合
def unite(x,y,par,rank,size):
    x = find(x,par)
    y = find(y,par)
    
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
def same(x,y,par):
    return find(x,par) == find(y,par)

########################################
n = int(input())
a = list(map(int,input().split()))

par = [0]*n #親
for i in range(n):
    par[i] = i
rank = [1]*n #深さ
size = [1]*n #size[i]:iを根とするグループのサイズ

b = [0]*(n+1) #b[i]:iがaにおいて何番目か
for i in range(n):
    b[a[i]]=i

ans = 0
for i in range(n,0,-1):
    k = b[i]
    left = 0
    right = 0
    if k-1>=0 and a[k-1]>a[k]:
        left =  size[find(k-1,par)]
        unite(k-1,k,par,rank,size)
    if k+1<=n-1 and a[k+1]>a[k]:
        right = size[find(k+1,par)]
        unite(k+1,k,par,rank,size)
    ans += (left+1)*(right+1)*a[k]

print(ans)
    