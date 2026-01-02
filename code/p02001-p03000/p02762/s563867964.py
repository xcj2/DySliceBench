def find(x): #xの根を求める
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def unite(x,y): #xとyの属する集合の併合
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

def same(x,y): #xとyが同じ集合に属するかの判定
    return find(x) == find(y)

def size(x): #xが属する集合の個数
    return -par[find(x)]

N,M,K = map(int, input().split())
par = [-1]*(N+1)
fri = [[] for i in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    fri[a].append(b)
    fri[b].append(a)
    unite(a,b)

bro = [[] for i in range(N+1)]
for i in range(K):
    c,d = map(int,input().split())
    bro[c].append(d)
    bro[d].append(c)

ans = [0]*N
for i in range(1,N+1):
    ans[i-1] = size(i)-1
    for f in fri[i]:
        if same(f,i): ans[i-1] -= 1
    for b in bro[i]:
        if same(b,i): ans[i-1] -= 1

# print(par)
ans = list(map(str,ans))
print(" ".join(ans))