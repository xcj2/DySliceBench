import sys
input = lambda: sys.stdin.readline().rstrip()

N,M = map(int, input().split())

def find(x):
    if parents[x] < 0:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if parents[x] > parents[y]:
        x,y = y, x

    parents[x] += parents[y]
    parents[y] = x 

def same(x,y):
    return find(x) == find(y)

edges = []
for i in range(M):
    a, b = map(int, input().split())
    edges.append((a-1,b-1))

ans = 0
for i in range(M):
    parents = [-1] * N
    for j in range(M):
        if i == j:
            continue
        s, e = edges[j]
        union(s, e)
    a, b = edges[i]
    if not same(a, b):
        ans += 1
print(ans)