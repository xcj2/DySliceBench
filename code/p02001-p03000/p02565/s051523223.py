class DiGraph:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.rev = [[] for _ in range(n)]
        self.deg = [0 for _ in range(n)]

    def add_edge(self, fr, to):
        self.graph[fr].append(to)
        self.rev[to].append(fr)
        self.deg[to] += 1

    def scc_ids(self):
        group = [None for _ in range(self.n)]
        used = [0 for _ in range(self.n)]
        order = []
        for s in range(self.n):
            if not used[s]:
                stack = [s]
                used[s] = 1
                while stack:
                    node = stack.pop()
                    movable = False
                    for adj in self.graph[node]:
                        if not used[adj]:
                            movable = True
                            used[adj] = 1
                            stack.append(node)
                            stack.append(adj)
                            break
                    if not movable:
                        order.append(node)
        used = [0 for _ in range(self.n)]
        count = 0
        for s in order[::-1]:
            if not used[s]:
                stack = [s]
                group[s] = count
                while stack:
                    node = stack.pop()
                    used[node] = 1
                    for adj in self.rev[node]:
                        if not used[adj]:
                            group[adj] = count
                            stack.append(adj)
                count += 1
        return group, count


class TwoSAT:
    def __init__(self, n):
        self.n = n
        self.res = [0] * self.n
        self.scc = DiGraph(2 * n)

    def add_clause(self, i: int, f: bool, j: int, g: bool):  # (x_i = f) V (x_j = g)
        self.scc.add_edge(2 * i + (not f), 2 * j + g)
        self.scc.add_edge(2 * j + (not g), 2 * i + f)

    def satisfiable(self):
        group, cnt = self.scc.scc_ids()
        for i in range(self.n):
            if group[2 * i] == group[2 * i + 1]:
                return False
            self.res[i] = (group[2 * i] > group[2 * i + 1])
        return True

    def result(self):
        return self.res


N, D = map(int, input().split())
XY = [tuple(map(int, input().split())) for _ in range(N)]

ts = TwoSAT(N)

for i in range(N-1):
    x1, y1 = XY[i][0], XY[i][1]
    for j in range(i+1, N):
        x2, y2 = XY[j][0], XY[j][1]

        if abs(x1 - x2) < D:
            ts.add_clause(i, True, j, True)
        if abs(x1 - y2) < D:
            ts.add_clause(i, True, j, False)
        if abs(y1 - x2) < D:
            ts.add_clause(i, False, j, True)
        if abs(y1 - y2) < D:
            ts.add_clause(i, False, j, False)

if ts.satisfiable():
    print('Yes')
    res = ts.result()
    for i in range(N):
        print(XY[i][0 if res[i] else 1])
else:
    print('No')
