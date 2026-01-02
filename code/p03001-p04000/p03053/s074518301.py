from collections import deque
h, w = map(int, input().split())
n = h*w


def to_v(i, j):
    return i*w+j


init_vs = []
for i in range(h):
    for j, x in enumerate(input()):
        if x == '#':
            init_vs.append(to_v(i, j))


INF = 10**18
dist = [INF]*n
for v in init_vs:
    dist[v] = 0


def generate_v2(v):
    i, j = divmod(v, w)
    if 0 < i:
        yield v-w
    if i < h-1:
        yield v+w
    if 0 < j:
        yield v-1
    if j < w-1:
        yield v+1


def bfs(init_vs):
    next_v = deque([*init_vs])
    while next_v:
        v = next_v.popleft()
        for v2 in generate_v2(v):
            if dist[v2] <= dist[v]+1:
                continue
            dist[v2] = dist[v]+1
            next_v.append(v2)


bfs(init_vs)
print(max(dist))