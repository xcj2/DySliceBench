import sys

input = sys.stdin.readline


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def func(N, mod):
    F = [1]
    for i in range(1, N + 1):
        F.append(F[-1] * i % mod)
    return F


INV = {}


def inv(a, mod):
    if a in INV:
        return INV[a]
    r = pow(a, mod - 2, mod)
    INV[a] = r
    return r


def C(F, a, b, mod):
    return F[a] * inv(F[b], mod) * inv(F[a - b], mod) % mod


class UF:
    def __init__(self, N):
        self.parent = [i for i in range(N)]

    def get_parent(self, a):
        p = self.parent[a]
        if a == p:
            return a

        q = self.get_parent(p)
        self.parent[a] = q
        return q

    def make_pare(self, a, b):
        pa = self.get_parent(a)
        pb = self.get_parent(b)
        if pa != pb:
            self.parent[pa] = pb
            self.parent[a] = pb

    def is_pare(self, a, b):
        return self.get_parent(a) == self.get_parent(b)


def main():
    N, M = read_values()
    P = read_list()
    F = [0] * N

    W = [tuple(read_values()) for _ in range(M)]
    U = UF(N)
    for a, b in W:
        a -= 1
        b -= 1
        U.make_pare(a, b)

    res = 0
    for p in P:
        p -= 1
        if U.is_pare(p, P[p] - 1):
            res += 1
    print(res)


if __name__ == "__main__":
    main()

