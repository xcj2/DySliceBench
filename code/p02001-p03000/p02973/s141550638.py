class Multiset:
    def __init__(self, N):
        self.N = N
        self.tree = [0] * (N + 1)
        self.bisect_K = [1 << k for k in reversed(range(N.bit_length()))]

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.N:
            self.tree[i] += x
            i += i & -i

    def bisect(self, w):
        if w <= 0:
            return 0
        bit, N = self.tree, self.N
        i = 0
        for k in self.bisect_K:
            ni = i + k
            if ni <= N and bit[ni] < w:
                w -= bit[ni]
                i = ni
        return i + 1

    def insert(self, x):
        self.add(x, 1)

    def erase(self, x):
        self.add(x, -1)

    def lower_bound(self, x):
        return self.bisect(self.sum(x))

    def size(self):
        return self.sum(self.N)


def main():

    # https://atcoder.jp/contests/abc134/tasks/abc134_e

    N, *A = map(int, open(0).read().split())

    memo = {a: i for i, a in enumerate(sorted(set(A)), 1)}
    M = len(memo)

    ms = Multiset(M)
    for b in (memo[a] for a in A):
        i = ms.lower_bound(b - 1)
        if i != 0:
            ms.erase(i)
        ms.insert(b)

    print(ms.size())


if __name__ == '__main__':
    main()
