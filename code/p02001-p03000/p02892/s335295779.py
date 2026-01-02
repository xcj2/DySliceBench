import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
V = []
for i in range(N):
    V.append(list(map(int, input()[:-1])))

INF = float('inf')

def is_bipartite_graph():
    team = [0] * N
    valid = True
    q = deque()
    q.append(0)
    team[0] = 1
    while valid and len(q):
        u = q.popleft()
        for v, e in enumerate(V[u]):
            if e:
                if not team[v]:
                    team[v] = team[u]%2 + 1
                    q.append(v)
                else:
                    if (team[v] - team[u])%2 == 0:
                        valid = False
                        break
    return valid


def get_distances(s):
    q = deque()
    q.append(s)
    d = [INF] * N
    d[s] = 0
    while len(q):
        u = q.popleft()
        for v, e in enumerate(V[u]):
            if e:
                if d[v] > d[u] + 1:
                    d[v] = d[u] + 1
                    q.append(v)
    return d


def get_diameter():
    dmax = 0
    for i in range(N):
        d = get_distances(i)
        dmax = max(max(d), dmax)
    return dmax


if is_bipartite_graph():
    print(get_diameter()+1)
else:
    print(-1)
