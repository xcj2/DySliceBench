from collections import deque
n, m = map(int, input().split())


def find(x):
    if par[x] < 0:
        return x
    par[x] = find(par[x])
    return par[x]

def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return
    if par[x] > par[y]:
        x, y = y, x
    par[x] += par[y]
    par[y] = x

def same(x, y):
    return find(x) == find(y)

def size(x):
    return par[find(x)]

node_list = []
for i in range(m):
    node_list.append([int(x) for x in input().split()])

ans = 0
for i in range(m):
    par = [-1 for _ in range(n)]
    for j in range(m):
        if i == j:
            continue
        else:
            union(node_list[j][0]-1, node_list[j][1]-1)
    limit = 2
    flag = False
    for value in par:
        if value < 0:
            limit -= 1
        if not limit:
            flag = True
            break
    if flag:
        ans += 1
print(ans)