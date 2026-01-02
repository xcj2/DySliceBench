import sys

input = sys.stdin.readline
N, M = map(int, input().split())
pair = {}
rank = {}
def root(x):
    if x == pair[x]:
        return x
    else:
        pair[x] = root(pair[x])
    return pair[x]

def unite(x, y):
    rx = root(x)
    ry = root(y)
    if rx == ry:
      return
    if rx > ry:
        pair[rx] = pair[ry]
    else:
        pair[ry] = pair[rx]

def same(x, y):
    rx = root(x)
    ry = root(y)
    return rx == ry

for i in range(1, N+1):
    pair.setdefault(i, i)

for i in range(1, N+1):
    rank.setdefault(i, 0)

for i in range(M):
    x, y, z = map(int, input().split())
    if not same(x, y):
        if x < y:
            unite(x, y)
        else:
            unite(y, x)
cnt = set()
for k, y in pair.items():
    y = root(y)
    cnt.add(y)
print(len(cnt))
