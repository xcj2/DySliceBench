import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p = list(map(int, input().split()))

parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)

def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

def same_check(x, y):
    return find(x) == find(y)

for i in range(m):
    x, y = map(int, input().split())
    union(p[x - 1], p[y - 1])
ans = 0
for i in range(n):
    if same_check(i + 1, p[i]):
        ans += 1
print(ans)