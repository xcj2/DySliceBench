import sys
import heapq


def link(x, y):
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]


def unite(x, y):
    link(find_set(x), find_set(y))


def same(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return True
    else:
        return False


h = []

line = sys.stdin.readline()
v, e = map(int, line.split())
p = [i for i in range(v)]
rank = [0 for _ in range(v)]

for i in range(e):
    line = sys.stdin.readline()
    s, t, w = map(int, line.split())
    heapq.heappush(h, (w, s, t))

s = 0
for i in range(e):
    elm = heapq.heappop(h)
    if not same(elm[1], elm[2]):
        s = s + elm[0]
        unite(elm[1], elm[2])

print(s)

