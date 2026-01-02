n, m = map(int, input().split())
parents = [-1] * n

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
    else:
        if parents[x] > parents[y]:
            x, y = y, x
        parents[x] += parents[y]
        parents[y] = x
        return True

def size(x):
    return -parents[find(x)]

for _ in range(m):
    a, b = map(int, input().split())
    unite(a - 1, b - 1)
max = 0
for x in range(n):
    s = size(x)
    if s > max:
        max = s
print(max)