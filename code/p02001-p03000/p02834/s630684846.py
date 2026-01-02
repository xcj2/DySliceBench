import sys


def inpl():
    return list(map(int, input().split()))


def set_depth(i):
    for e in edge[i]:
        if depth[e] != -1:
            continue
        depth[e] = depth[i] + 1
        parent[e] = i
        set_depth(e)
    return


def get_root_v(can_depth, u):
    if depth[u] == can_depth:
        return u
    else:
        return get_root_v(can_depth, parent[u])


def find_max_depth(v):
    if len(edge[v]) == 1 and parent[v] == edge[0]:
        return depth[v]

    tmp = depth[v]
    for e in edge[v]:
        if parent[v] == e:
            continue
        else:
            tmp = max(tmp, find_max_depth(e))
    return tmp


sys.setrecursionlimit(2 * 10**6)

N, u, v = inpl()
AB = [inpl() for _ in range(N - 1)]
edge = [[] for i in range(N + 1)]
for a, b in AB:
    edge[a].append(b)
    edge[b].append(a)

depth = [-1 for i in range(N + 1)]
depth[v] = 0

parent = [-1 for i in range(N + 1)]

set_depth(v)

can_depth = depth[u] - (depth[u] - 1) // 2
root_v = get_root_v(can_depth, u)

print(find_max_depth(root_v) - 1)
