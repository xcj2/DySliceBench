n, m, k = map(int, input().split())
a_m, b_m = [], []
c_k, d_k = [], []
def minus(x):
    return int(x)-1

friends_list = [[] for i in range(n)]
block_list = [[] for i in range(n)]
for i in range(m):
    a_m.append(0)
    b_m.append(0)
    a_m[i], b_m[i] = map(minus, input().split())
    friends_list[a_m[i]].append(b_m[i])
    friends_list[b_m[i]].append(a_m[i])
for i in range(k):
    c_k.append(0)
    d_k.append(0)
    c_k[i], d_k[i] = map(minus, input().split())
    block_list[c_k[i]].append(d_k[i])
    block_list[d_k[i]].append(c_k[i])

# どのグループに属しているかを返す
def find(x):
    if parents[x] < 0:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    if parents[x] > parents[y]:
        x, y = y, x
    parents[x] += parents[y]
    parents[y] = x
    return True

def union_size(x):
    return -parents[find(x)]

def blocks_in_union(x):
    count = 0
    for block in block_list[x]:
        if find(x) == find(block):
            count += 1
    return count

parents =[ -1 for i in range(n)]
for i in range(m):
    unite(a_m[i], b_m[i])
for i in range(n):
    print(union_size(i)-1-len(friends_list[i])-blocks_in_union(i), end=' ')
