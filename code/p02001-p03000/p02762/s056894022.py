import sys
sys.setrecursionlimit(100000)


class UnionFind:

    def __init__(self, N):
        self._N = N
        self._parents = [-1 for n in range(N)]
        self._size = [1 for n in range(N)]

    def is_root(self, x):
        return self._parents[x] < 0

    def size(self, x):
        assert self.is_root(x)
        return self._size[x]

    def find(self, x):
        if self.is_root(x):
            return x
        else:
            self._parents[x] = self.find(self._parents[x])
            return self._parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self._size[x] > self._size[y]:
            x, y = y, x

        self._parents[y] = x
        self._size[x] += self._size[y]
        self._size[y] = None


def solve():

    N, M, K = map(int, input().split())

    A = [0 for m in range(M)]
    B = [0 for m in range(M)]
    tree = UnionFind(N)
    for m in range(M):
        A[m], B[m] = map(int, input().split())
        tree.union(A[m]-1, B[m]-1)

    n_friends = [0 for n in range(N)]
    for m in range(M):
        root_a, root_b = tree.find(A[m]-1), tree.find(B[m]-1)
        assert root_a == root_b
        n_friends[A[m]-1] += 1
        n_friends[B[m]-1] += 1

    C = [0 for k in range(K)]
    D = [0 for k in range(K)]
    n_blocks_in_group = [0 for n in range(N)]
    for k in range(K):
        C[k], D[k] = map(int, input().split())
        root_c, root_d = tree.find(C[k]-1), tree.find(D[k]-1)
        if root_c == root_d:
            n_blocks_in_group[C[k]-1] += 1
            n_blocks_in_group[D[k]-1] += 1

    res = []
    for n in range(N):
        n_cand = tree.size(tree.find(n)) - n_friends[n] - n_blocks_in_group[n] - 1
        res.append(str(n_cand))
    print(' '.join(res))


solve()
