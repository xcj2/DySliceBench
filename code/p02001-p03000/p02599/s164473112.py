from collections import defaultdict
import sys
def read():
    return sys.stdin.readline().rstrip()
def main():
    N, Q = map(int, read().split())
    C = list(map(int, read().split()))
    E = defaultdict(list)

    D = [-1] * (N + 1)
    for i in range(N):
        D_i = D[C[i]]
        if D_i != -1:
            E[D_i].append((D_i, i))
        D[C[i]] = i

    F = defaultdict(list)
    for i in range(Q):
        l, r = map(int, input().split())
        F[l-1].append((r - 1, i))



    # Binary Indexed Tree (Fenwick Tree)
    class BIT:
        def __init__(self, n):
            self.n = n
            self.data = [0] * (n + 1)
            self.el = [0] * (n + 1)

        def sum(self, i):
            s = 0
            while i > 0:
                s += self.data[i]
                i -= i & -i
            return s

        def add(self, i, x):
            # assert i > 0
            self.el[i] += x
            while i <= self.n:
                self.data[i] += x
                i += i & -i

        def get(self, i, j=None):
            if j is None:
                return self.el[i]
            return self.sum(j) - self.sum(i)

    ANS = [0] * Q
    d = BIT(N)
    for x in range(N - 1, -1, -1):
        for e in E[x]:
            d.add(e[1], 1)
        for f in F[x]:
            ANS[f[1]] = f[0] - x + 1 - d.sum(f[0])

    for i in range(Q):
        print(ANS[i])

if __name__ == '__main__':
    main()
