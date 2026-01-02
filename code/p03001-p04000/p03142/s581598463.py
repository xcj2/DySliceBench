from collections import defaultdict, deque


def read():
    return int(input())


def readlist():
    return list(map(int, input().split()))


def readmap():
    return map(int, input().split())


N, M = readmap()
es = []
for _ in range(N - 1 + M):
    a, b = readmap()
    es.append([a, b])

v = N
n = N - 1 + M
# es = [[int(x) for x in input().split()] for _ in range(n)]

outs = defaultdict(list)
ins = defaultdict(int)
for v1, v2 in es:
    outs[v1].append(v2)
    ins[v2] += 1

q = deque(v1 for v1 in range(v) if ins[v1] == 0)
res = []
while q:
    v1 = q.popleft()
    res.append(v1)
    for v2 in outs[v1]:
        ins[v2] -= 1
        if ins[v2] == 0:
            q.append(v2)

del res[0]
topo = res
inv_topo = [0] * N
for i in range(1, N+1):
    inv_topo[topo[i-1]-1] = i

parent = [0 for _ in range(N+1)]
for edge in es:
    child = edge[1]
    if parent[child] == 0:
        parent[child] = edge[0]
    else:
        if inv_topo[parent[child] - 1] < inv_topo[edge[0] - 1]:
            parent[child] = edge[0]

del parent[0]
for p in parent:
    print(p)

