n, m = map(int, input().split())
p = list(map(lambda x: x-1, map(int, input().split())))

follow = [i for i in range(n)]
num = [1]*n
def root_index_of(x):
    r = x
    while follow[r] != r:
        r = follow[r]
    return r

def connected(x, y):
    return root_index_of(x) == root_index_of(y)

def connect(x, y):
    rx = root_index_of(x)
    ry = root_index_of(y)

    if rx == ry:
        return

    if num[rx] < num[ry]:
        follow[rx] = ry
        follow[x] = ry
        num[ry] += num[rx]
    else:
        follow[ry] = rx
        follow[y] = rx
        num[rx] += num[ry]

for i in range(m):
    x, y = map(lambda x: x-1, map(int, input().split()))
    connect(p[x], p[y])

ans = 0
for i in range(n):
    if connected(i, p[i]):
        ans += 1
print(ans)
