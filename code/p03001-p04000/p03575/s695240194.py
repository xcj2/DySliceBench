N, M = [int(_) for _ in input().split()]

paths = [[0] * (N + 1) for _ in range(N + 1)]

edges = []
for i in range(M):
    a, b = [int(_) for _ in input().split()]
    paths[a][b] = 1
    paths[b][a] = 1
    edges.append((a, b))


class UF:
    def __init__(self, v):
        self.parent = None
        self.val = v

    @property
    def root(self):
        if not self.parent:
            return self
        return self.parent.root

    def __str__(self):
        if self.parent:
            return str(self.val) + ' ' + str(self.parent.val)
        return str(self.val) + ' None'


def merge(u1, u2):
    r1 = u1.root
    r2 = u2.root
    if r1 == r2:
        return
    r1.parent = r2


def chk(a, b):
    nodes = [UF(i) for i in range(N + 1)]
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            if paths[i][j]:
                merge(nodes[i], nodes[j])
    return int(nodes[a].root != nodes[b].root)


ans = 0
for e in edges:
    paths[e[0]][e[1]] = 0
    paths[e[1]][e[0]] = 0
    ans += chk(e[0], e[1])
    paths[e[0]][e[1]] = 1
    paths[e[1]][e[0]] = 1
print(ans)