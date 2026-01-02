import itertools

n = int(input())
A = [list(map(int, input().strip().split(' '))) for _ in range(n)]
uvc = [] # A list of tuples of start, end, and cost
for i in range(n-1):
    for j in range(i+1, n):
        if A[i][j] >= 0:
            uvc.append((i, j, A[i][j]))

# コストでソート
uvc.sort(key=lambda x: x[2])

uf = list(range(n))

def find_root(x):
    global uf
    if x == uf[x]:
        return x
    else:
        uf[x] = find_root(uf[x])
        return uf[x]

def union(x, y):
    global uf
    uf[find_root(x)] = find_root(y)

def is_same_set(x, y):
    return find_root(x) == find_root(y)

def costs():
    global uvc
    for u, v, c in uvc:
        if not is_same_set(u, v):
            union(u, v)
            yield c
print(sum(itertools.islice(costs(), n - 1)))


