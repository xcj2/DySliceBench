def root(x):
    if(group[x] == x):
        return(x)
    else:
        group[x] = root(group[x])
        return(group[x])


def unite(x, y):
    x = root(x)
    y = root(y)
    if(x == y):
        return

    if(rank[x] < rank[y]):
        group[x] = y
    else:
        group[y] = x
        if(rank[x] == rank[y]):
            rank[x] += 1


def same(x, y):
    return(root(x) == root(y))


N, M = map(int, input().split())
N_list = list(map(int, input().split()))
for i in range(N):
    N_list[i] -= 1

group = [i for i in range(N)]
rank = [0 for i in range(N)]

for i in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    unite(x, y)


ans = 0
for i in range(N):
    if(same(i, N_list[i]) is True):
        ans += 1
print(ans)