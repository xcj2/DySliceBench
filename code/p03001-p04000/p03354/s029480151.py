N, M = map(int, input().split())
p = list(map(int, input().split()))
par = [i for i in range(N+1)]
rank = [0] * (N+1)
def find(x):
    if par[x] == x:
        return x
    else:
        #親を検索
        par[x] = find(par[x])
        return par[x]

def same_checker(x, y):
    return find(x) == find(y)

def union(x, y):
    x = find(x)
    y = find(y)
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

for i in range(M):
    x, y = map(int, input().split())
    union(x, y)
S = {}
for i in range(N):
    S[p[i]] = par[i+1]
ans = 0
for i in range(N):
    if same_checker(S[p[i]], S[i+1]):
        ans += 1

print(ans)
