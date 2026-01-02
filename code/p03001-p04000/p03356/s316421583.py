#UnionFind
def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def same(x, y):
    return find(x) == find(y)

def unite(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    else:
        if rank[x] < rank[y]:
            par[x] = y

        else:
            par[y] = x

            if rank[x] == rank[y]:
                rank[x] += 1

#main
n, m = map(int,input().split())
p = list(map(int,input().split()))
par = [i for i in range(n)]
rank = [0] * n

for i in range(m):
    x, y = map(int,input().split())
    unite(x - 1 , y - 1)
ans = 0
for i in range(n):
    if same(i, p[i] - 1):
        ans += 1

print(ans)
