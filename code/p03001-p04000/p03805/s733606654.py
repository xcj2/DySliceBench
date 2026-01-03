def get_args():
    N, M = map(int, input().split())
    A, B = [], []

    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # print(N, M)
    # print(A, B)

    return N, M, A, B


class Graph:
    def __init__(self, vertex_size):
        self.VERTEX_SIZE = vertex_size
        self.adjacency = [set() for i in range(self.VERTEX_SIZE)]

    def add_edge(self, a_i, b_i):
        self.adjacency[a_i].add(b_i)
        self.adjacency[b_i].add(a_i)

    def get_adj(self, i):
        return self.adjacency[i]

    def vertexes_size(self):
        return self.VERTEX_SIZE

    def edges_size(self):
        raise NotImplemented()


def solve(N, M, A, B):
    g = Graph(8 + 2)

    for i in range(M):
        g.add_edge(A[i], B[i])

    marked = [False for _ in range(N + 1)]

    def dfs(i):
        marked[i] = True

        c = 0
        if marked.count(True) == N:
            c += 1

        for a in g.get_adj(i):
            if not marked[a]:
                c += dfs(a)

        marked[i] = False
        return c

    res = dfs(1)
    return res


if __name__ == '__main__':
    res = solve(*get_args())
    print(res)
