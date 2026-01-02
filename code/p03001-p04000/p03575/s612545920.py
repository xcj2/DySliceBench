N, M = map(int, input().split())
G = [[] for i in range(N)]
S = []
for i in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    S.append((a, b))


parent = [i for i in range(N)]
rank = [0] * N


def find(i):
    if parent[i] == i:
        return i
    else:
        parent[i] = find(parent[i])
        return parent[i]


def same(x, y):
    return find(x) == find(y)


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return

    if rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1

num = 0
for a, b in S:
    parent = [i for i in range(N)]
    rank = [0] * N
    for c, d in S:
        if c == a and b == d:
            continue
        else:
            unite(c, d)

    flag = False
    for i in range(N):
        if flag:
            break
        for j in range(N):
            if not same(i, j):
                flag = True
                break

    if flag:
        num += 1


print(num)

