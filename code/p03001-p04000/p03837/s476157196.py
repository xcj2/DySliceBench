import sys
import bisect

input = sys.stdin.readline
sys.setrecursionlimit(100000)
mod = 10 ** 9 + 7
# mod = 998244353


def read_values():
    return map(int, input().split())


def read_index():
    return map(lambda x: int(x) - 1, input().split())


def read_list():
    return list(read_values())


def read_lists(N):
    return [read_list() for n in range(N)]


class UF:
    def __init__(self, N):
        self.state = [-1] * N
        self.rank = [0] * N
        self.num_group = N

    def get_parent(self, a):
        p = self.state[a]
        if p < 0:
            return a

        q = self.get_parent(p)
        self.state[a] = q
        return q

    def make_pair(self, a, b):
        pa = self.get_parent(a)
        pb = self.get_parent(b)
        if pa == pb:
            return

        if self.rank[pa] > self.rank[pb]:
            pa, pb = pb, pa
            a, b = b, a
        elif self.rank[pa] == self.rank[pb]:
            self.rank[pb] += 1

        self.state[pb] += self.state[pa]
        self.state[pa] = pb
        self.state[a] = pb
        self.num_group -= 1

    def is_pair(self, a, b):
        return self.get_parent(a) == self.get_parent(b)

    def get_size(self, a):
        return -self.state[self.get_parent(a)]


class V:
    def __init__(self, f, v=None):
        self.f = f
        self.v = v

    def __str__(self):
        return str(self.v)

    def ud(self, n):
        if n is None:
            return

        if self.v is None:
            self.v = n
            return
        self.v = self.f(self.v, n)


def main():
    N, M = read_values()
    L = []
    D = [[10 ** 10 for _ in range(N)] for __ in range(N)]
    for _ in range(M):
        a, b, c = read_values()
        a -= 1
        b -= 1
        D[a][b] = c
        D[b][a] = c
        L.append((c, a, b))
    L.sort()

    for i in range(N):
        D[i][i] = 0

    for k in range(N):
        for i in range(N):
            for j in range(N):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    res = 0
    for c, a, b in L:
        if D[a][b] < c:
            res += 1

    print(res)


if __name__ == "__main__":
    main()
