n, m = map(int, input().split())

par = [i for i in range(n)]
rank = [0 for i in range(n)]
diff_weight = [0 for i in range(n)]


def root(x):
    if par[x] == x:
        return x
    r = root(par[x])
    diff_weight[x] += diff_weight[par[x]]
    par[x] = r
    return par[x]

def issame(x, y):
    return root(x) == root(y)

def weight(x):
    root(x)
    return diff_weight[x]

def diff(x, y):
    return weight(y) - weight(x)

def merge(x, y, w):
    w += weight(x)
    w -= weight(y)
    x = root(x)
    y = root(y)
    if x == y:
        return False
    if rank[x] < rank[y]:
        x, y = y, x
        w = -w
    if rank[x] == rank[y]:
        rank[x] += 1
    par[y] = x
    diff_weight[y] = w
    return True

for i in range(m):
    l, r, d = map(int, input().split())
    if issame(l-1, r-1):
        di = diff(l-1, r-1)
        if di != d:
            print("No")
            exit()
    else:
        merge(l-1, r-1, d)

print("Yes")