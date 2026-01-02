#!/usr/bin/env python3
# from collections import Counter

parent = None


def root(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = root(parent[a])
        return parent[a]


def is_same(a, b):
    return root(a) == root(b)


def unite(a, b):
    # print('before:',end='')
    # print(parent)
    ra = root(a)
    rb = root(b)
    # print(ra, rb, sep='|')
    if ra == rb:
        return
    parent[ra] = rb
# print('after:',end='')
# print(parent)


n, m = map(int, input().split())
grid = []

for i in range(m):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    grid.append((x, y))
    # grid[y][x] = 1

# print(grid)

ans = 0
for i in range(m):
    # print('-----------------------')
    parent = [k for k in range(n)]
    # print(parent)

    for j, e in enumerate(grid):
        # print(j, e, sep='#')
        if j == i:
            continue
        a, b = e
        unite(a, b)

    # print(grid[i], parent, sep='=')
    a, b = grid[i]
    if not is_same(a, b):
        # print(parent)
        ans += 1
    # print(parent)

print(ans)
