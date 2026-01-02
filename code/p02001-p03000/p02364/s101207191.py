# https://onlinejudge.u-aizu.ac.jp/problems/GRL_2_A
def root(x):
    if parent_map[x] == x:
        return x
    parent_map[x] = root(parent_map[x])
    return parent_map[x]


def same(x, y):
    return root(x) == root(y)


def unite(x, y):
    x = root(x)
    y = root(y)
    parent_map[x] = y


v, e = list(map(int, input().split()))
edges = [list(map(int, input().split())) for i in range(e)]
edges.sort(key=lambda x: x[2])
parent_map = [i for i in range(v)]

result = 0
for s, t, w in edges:
    if not same(s, t):
        result += w
        unite(s, t)
print(result)

