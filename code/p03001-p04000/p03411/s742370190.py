from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

N = int(input())

R = []
for _ in range(N):
    x, y = map(int, input().split())
    R.append(Point(x, y))

B = []
for _ in range(N):
    x, y = map(int, input().split())
    B.append(Point(x, y))

E = [[] for _ in range(N)]
for i, r in enumerate(R):
    for j, b in enumerate(B):
        if r.x < b.x and r.y < b.y:
            E[i].append(j)


class BipartiteMatching:
    def __init__(self, max_u: int, edges):
        self.max_u = max_u
        self.edges = edges  # u->vの隣接行列
        self.__match = None

    def dfs(self, v: int, visited: set) -> bool:
        for u in self.edges[v]:
            if u in visited:
                continue
            visited.add(u)

            if self.__match[u] == -1 or self.dfs(self.__match[u], visited):
                self.__match[u] = v
                return True
        return False

    def execute(self):
        self.__match = [-1 for _ in range(self.max_u)]
        return sum(self.dfs(u, set()) for u in range(self.max_u))


print(BipartiteMatching(N, E).execute())
