# Kruskal's Algorithm

def kruskal():
    '''
    最小全域木のコストを求める
    '''
    cost = 0
    edge.sort()

    for c, u, v in edge:
        if same(u, v):
            continue
        union(u, v)
        cost += c

    return cost


def find(x):
    '''
    xの根を求める
    '''
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def union(x, y):
    '''
    xとyの属する集合を併合する
    '''
    x = find(x)
    y = find(y)
    
    if x == y:
        return False

    if par[x] > par[y]:
        x, y = y, x

    par[x] += par[y]
    par[y] = x
    return True


def same(x, y):
    '''
    xとyが同じ集合に属するかを判定する
    '''
    return find(x) == find(y)


################################
n, w = map(int, input().split())  # n:頂点数　w:辺の数

par = [-1] * n  # 根: -size, 葉: 親の頂点
edge = []       # edge[i]:iから出る辺の[重み,行先]の配列
for _ in range(w):
    x, y, z = map(int, input().split())
    edge.append([z, x, y])

print(kruskal())
