from itertools import accumulate
def find(x):
    if par[x] == x:
        return x
    else:
        return find(par[x])

def unite(x, y):
    x = find(x)
    y = find(y)
    
    if x != y:
        if rank[x] < rank[y]:
            par[x] = y
            size[y] += size[x]
        else:
            par[y] = x
            size[x] += size[y]
            if rank[x] == rank[y]:
                rank[x] += 1

def same(x, y):
    return find(x) == find(y)

N, M = map(int, input().split())
AB = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]

par = list(range(N))
rank = [1] * N
size = [1] * N

ans = [0] * M
for i in range(M-1, -1, -1):
    x = find(AB[i][0])
    y = find(AB[i][1])
    if x != y:
        ans[i] = size[x] * size[y]
        unite(x, y)
        
for i in accumulate(ans):
    print(i)
        