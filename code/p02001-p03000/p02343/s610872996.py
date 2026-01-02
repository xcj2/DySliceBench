n, q = map(int, input().split())
# initialize
par = [-1] * n
rank = [0] * n

# Union Find Tree
def find(x):
    """ 根ノードの値を見つけて返す """
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def unite(x, y):
    """xとyを結合する"""
    rootx = find(x)
    rooty = find(y)

    if rootx == rooty:
        return False
    else:
        if rank[rootx] < rank[rooty]:
            par[rootx] = rooty
        else:
            par[rooty] = rootx
            if rank[rootx] == rank[rooty]: rank[rootx] += 1
        return True

def same(x, y):
    return find(x) == find(y)


for _ in range(q):
    com, x, y = map(int, input().split())
    if com == 0:
        unite(x, y)
    elif com == 1:
        if same(x, y):
            print(1)
        else:
            print(0)

