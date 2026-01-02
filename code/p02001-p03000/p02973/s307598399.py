class BIT:
    def __init__(self, N):
        self.size = N
        self.tree = [0] * (N + 1)
        self.bisect_K = [1 << k for k in reversed(range(N.bit_length()))]

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def bisect(self, w):
        if w <= 0:
            return 0
        bit, N = self.tree, self.size
        i = 0
        for k in self.bisect_K:
            if i + k <= N and bit[i + k] < w:
                i += k
                w -= bit[i]
        return i + 1


class Multiset:
    def __init__(self, N):
        self.N = N
        self.bit = BIT(N)

    def insert(self, x):
        self.bit.add(x, 1)

    def erase(self, x):
        self.bit.add(x, -1)

    def lower_bound(self, x):
        return self.bit.bisect(self.bit.sum(x))

    def size(self):
        return self.bit.sum(self.N)


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
