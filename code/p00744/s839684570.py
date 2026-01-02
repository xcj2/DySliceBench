from collections import deque


class Dinic(object):
    __slots__ = ["inf", "v_count", "edges", "iter", "level"]

    def __init__(self, v_count: int, edges: list):
        self.inf = 10**9
        self.v_count = v_count
        self.edges = [[] for _ in [0]*v_count]
        self.iter = [0]*v_count
        self.level = None
        self._create_graph(edges)

    def _create_graph(self, _edges):
        edges = self.edges
        for origin, dest, cap in _edges:
            edges[origin].append([dest, cap, len(edges[dest])])
            edges[dest].append([origin, 0, len(edges[origin])-1])

    def solve(self, source: int, sink: int):
        max_flow = 0

        while True:
            self.bfs(source)
            if self.level[sink] < 0:
                return max_flow

            self.iter = [0]*self.v_count
            flow = self.dfs(source, sink, self.inf)

            while flow > 0:
                max_flow += flow
                flow = self.dfs(source, sink, self.inf)

    def bfs(self, source: int):
        level, edges = [-1]*self.v_count, self.edges
        level[source] = 0
        dq = deque([source])
        popleft, append = dq.popleft, dq.append

        while dq:
            v = popleft()
            for dest, cap, _rev in edges[v]:
                if cap > 0 > level[dest]:
                    level[dest] = level[v] + 1
                    append(dest)

        self.level = level

    def dfs(self, source: int, sink: int, flow: int) -> int:
        if source == sink:
            return flow
        while self.iter[source] < len(self.edges[source]):
            dest, cap, rev = edge = self.edges[source][self.iter[source]]
            if cap > 0 and self.level[source] < self.level[dest]:
                flowed = self.dfs(dest, sink, flow if flow < cap else cap)
                if flowed > 0:
                    edge[1] -= flowed
                    self.edges[dest][rev][1] += flowed
                    return flowed
            self.iter[source] += 1

        return 0


def get_prime_set(ub):
    from itertools import chain
    from math import sqrt

    if ub < 4:
        return ({}, {}, {2}, {2, 3})[ub]

    ub, ub_sqrt = ub+1, int(sqrt(ub))+1
    primes = {2, 3} | set(chain(range(5, ub, 6), range(7, ub, 6)))
    du = primes.difference_update
    for n in chain(range(5, ub_sqrt, 6), range(7, ub_sqrt, 6)):
        if n in primes:
            du(range(n*3, ub, n*2))

    return primes


if __name__ == "__main__":
    from math import sqrt
    from collections import defaultdict
    primes = get_prime_set(int(sqrt(10**7))+1)
    answer = []
    append_answer = answer.append

    while True:
        M, N = map(int, input().split())
        if not M*N:
            break

        source, sink = M+N, M+N+1
        edges, blue, red = [], [], []
        for i in range(M):
            edges.append((i, sink, 1))
        for i in range(M, M+N):
            edges.append((source, i, 1))
        divisors = defaultdict(set)
        index = 0

        # blue
        while index < M:
            for num in map(int, input().split()):
                for p in filter(lambda x: num % x == 0, primes):
                    divisors[p].add(index)
                    while num % p == 0:
                        num //= p
                if num > 1:
                    divisors[num].add(index)
                index += 1

        # red
        while index < M+N:
            for num in map(int, input().split()):
                neighbors = set()
                update = neighbors.update
                for p in filter(lambda x: num % x == 0, primes):
                    update(divisors[p])
                    while num % p == 0:
                        num //= p
                if num > 1:
                    update(divisors[num])

                for dest in neighbors:
                    edges.append((index, dest, 1))

                index += 1

        dinic = Dinic(sink+1, edges)
        append_answer(dinic.solve(source, sink))

    print(*answer, sep="\n")
