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
 
N,M,K = map(int,input().split())
#初期化
#根なら-size,子なら親の頂点
par = [-1]*(N+1)
 
friends = [[]for i in range(0,N+1,1)]
block = [[]for i in range(0,N+1,1)]
for i in range(0,M,1):
    a,b = map(int,input().split())
    friends[a].append(b)
    friends[b].append(a)
    unite(a,b)
for i in range(0,K,1):
    a,b=map(int,input().split())
    block[a].append(b)
    block[b].append(a)
 
countmem = [0]*N
for i in range(1,N+1,1):
    count = size(i)-1
    mem = []
    ma = mem.append
    for j in range(0,len(friends[i]),1):
        if same(i,friends[i][j]):
            count -=1
            ma(friends[i][j])
    for j in range(0,len(block[i]),1):
        if same(i,block[i][j]) and not(block[i][j] in mem):
            count -=1
    countmem[i-1]=count
 
print(*countmem)