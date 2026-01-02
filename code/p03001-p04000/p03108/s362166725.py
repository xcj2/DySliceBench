def uf_init(n):
    return list(range(n)), [1]*n

def uf_root(ufdata, x):
    uf,_ = ufdata
    update_node_arr = []
    while(uf[x] != x):
        update_node_arr.append(x)
        x = uf[x]
    for y in update_node_arr:
        uf[y] = x
    return x

def uf_same(ufdata, x, y):
    return uf_root(ufdata, x) == uf_root(ufdata, y)

def uf_size(ufdata, x):
    _,usize = ufdata
    return usize[uf_root(ufdata, x)]

def uf_unite(ufdata, x, y):
    uf,usize = ufdata
    x = uf_root(ufdata, x)
    y = uf_root(ufdata, y)
    if x == y:
        return
    xysize = uf_size(ufdata, x) + uf_size(ufdata, y)
    if uf_size(ufdata, x) > uf_size(ufdata, y):
        uf[y] = x
        usize[x] = xysize
    else:
        uf[x] = y
        usize[y] = xysize

N,M = (int(x) for x in input().split())

uf = uf_init(N)

AB_arr = []
for _ in range(M):
    AB_arr.append(tuple((int(x)-1 for x in input().split())))

ans = N*(N-1)//2
ans_arr = [ans]
for A,B in reversed(AB_arr):
    if not uf_same(uf, A, B):
        ans -= uf_size(uf, A) * uf_size(uf, B)
    ans_arr.append(ans)
    uf_unite(uf, A, B)

for ans in reversed(ans_arr[:-1]):
    print(ans)


