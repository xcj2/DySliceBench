def uf_init(n):
    return list(range(n))

def uf_root(uf, x):
    if uf[x] != x:
        uf[x] = uf_root(uf, uf[x])
    return uf[x]

def uf_same(uf, x, y):
    return uf_root(uf, x) == uf_root(uf, y)

def uf_unite(uf, x, y):
    x = uf_root(uf, x)
    y = uf_root(uf, y)
    if x == y:
        return
    uf[x] = y


N = int(input())

x_dict = {}
y_dict = {}
uf = uf_init(N)

xy_arr = []
for i in range(N):
    x,y = (int(x) for x in input().split())
    if x in x_dict:
        uf_unite(uf, i, x_dict[x])
    else:
        x_dict[x] = i
    if y in y_dict:
        uf_unite(uf, i, y_dict[y])
    else:
        y_dict[y] = i
    xy_arr.append((x,y))

unite_dict = {}
for i in range(N):
    ur = uf_root(uf, i)
    unite_dict.setdefault(ur, [set(), set()])
    unite_dict[ur][0].add(xy_arr[i][0])
    unite_dict[ur][1].add(xy_arr[i][1])

total_points = 0
for k,v in unite_dict.items():
    total_points += len(v[0])*len(v[1])

print(total_points-N)
