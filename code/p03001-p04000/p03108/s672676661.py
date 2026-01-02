#木の根を得る
def root(x):
    while par[x] >= 0:
        x = par[x]
    return x

#木の併合
def unite(x, y):
    rx = root(x)
    ry = root(y)
    if rx != ry:
        if rx > ry:
            rx, ry = ry, rx
        par[rx] += par[ry]
        par[ry] = rx

def size(x):
    return -par[root(x)]

def same(x, y):
    rx = root(x)
    ry = root(y)
    return rx == ry

N, M = map(int,input().split())
par = [-1]*N
K = []
for i in range(M):
    a, b = map(int, input().split())
    K.append([a-1, b-1])
K = K[::-1]

result = [0]
ans = 0
for i, j in K:
    if not same(i, j):
        a = size(i)
        b = size(j)
        unite(i, j)
        c = size(i)
        ans += c*(c-1)//2 - (a*(a-1)//2 + b*(b-1)//2)
    result.append(ans)

result = result[::-1]
for i in result[1:]:
    print(result[0] - i)