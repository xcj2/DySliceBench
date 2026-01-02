import sys
input = sys.stdin.readline
n, m = map(int, input().split())

parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)
weight = [0] * (n + 1)

def find(x):
    if parent[x] == x:
        return x
    else:
        y = find(parent[x])
        weight[x] += weight[parent[x]]
        parent[x] = y
        return y

def union(x, y, w):
    rx = find(x)
    ry = find(y)
    if rank[rx] < rank[ry]:
        parent[rx] = ry
        weight[rx] = w - weight[x] + weight[y]
    else:
        parent[ry] = rx
        weight[ry] = -w - weight[y] + weight[x]
        if rank[rx] == rank[ry]:
            rank[rx] += 1

def same_check(x, y):
    return find(x) == find(y)

def diff(x, y):
    return weight[x] - weight[y]

ans = "Yes"
for i in range(m):
    l, r, d = map(int, input().split())
    if same_check(l, r):
        if diff(l, r) != d:
            ans = "No"
            break
    else:
        union(l, r, d)
print(ans)