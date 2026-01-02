N,M,K = map(int,input().split())
Fri = [list(map(int,input().split())) for _ in range(M)]
Blo = [list(map(int,input().split())) for _ in range(K)]

#union-find
par = [i for i in range(N+1)]
relation = [1 for _ in range(N+1)] #自身を含む同グループの数
rank = [0 for _ in range(N+1)]
def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def unite(x,y):
    x,y = find(x),find(y)
    if x != y:
        if rank[x] < rank[y]:
            par[x] = y
            relation[y] += relation[x]
        else:
            par[y] = x
            relation[x] += relation[y]
            if rank[x] == rank[y]:
                rank[x] += 1

def same(x,y):
    return find(x) == find(y)

ans = [relation[find(i)] for i in range(N+1)]
for m in range(M):
    unite(Fri[m][0],Fri[m][1])
    ans[Fri[m][0]] -= 1
    ans[Fri[m][1]] -= 1

for k in range(K):
    if same(Blo[k][0],Blo[k][1]):
        ans[Blo[k][0]] -= 1
        ans[Blo[k][1]] -= 1

for i in range(1,N+1):
    ans[i] += (relation[find(i)] - 2)
    if i != 1:
        print(" ",end="")
    print(ans[i],end="")
