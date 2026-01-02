N,M = map(int,input().split())
info = [list(map(int,input().split())) for i in range(M)]
nodes = [-1]*N
diff_weight = [0]*N

def root(x):
    if nodes[x] < 0:
        return x
    root_x = root(nodes[x])
    diff_weight[x] += diff_weight[nodes[x]]
    nodes[x] = root_x
    return root_x

def weight(x):
    root(x)
    return diff_weight[x]

def unite(x,y,w):
    w += weight(x); w -= weight(y)
    x = root(x); y = root(y)
    if x == y:
        return
    rank_x = -nodes[x]; rank_y = -nodes[y]
    if rank_x >= rank_y:
        nodes[y] = x
        diff_weight[y] = w
        if rank_x == rank_y:
            nodes[x] -= 1
    else:
        nodes[x] = y
        diff_weight[x] = -w

def same(x,y):
    return root(x) == root(y)

def diff(x,y):
    return weight(y) - weight(x)

ans = "Yes"

for L,R,D in info:
    L -= 1; R -= 1
    unite(L,R,D)
    if diff(L,R) != D:
        ans = "No"
        break
print(ans)