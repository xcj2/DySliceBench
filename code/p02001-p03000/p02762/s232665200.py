n,m,k=map(int,input().split())
ab=[]
for i in range(m):
    a,b=map(int,input().split())
    ab.append((a-1,b-1))
cd=[]
for i in range(k):
    c,d=map(int,input().split())
    cd.append((c-1,d-1))

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

#初期化
#根なら-size,子なら親の頂点
par = [-1]*n
for a,b in ab:
    unite(a,b)
dp1=[0]*n
for i in range(n):
    dp1[i]=size(i)-1
for a,b in ab:
    dp1[a]-=1
    dp1[b]-=1
for c,d in cd:
    if same(c,d):
        dp1[c]-=1
        dp1[d]-=1
print(' '.join(map(str,dp1)))