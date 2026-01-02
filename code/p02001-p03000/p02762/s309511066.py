class UnionFind:

    def __init__(self, n):
        self.t = [-1] * (n + 1)

    def flatten(self):
        for i, _ in enumerate(self.t):
            self.find_root(i)

    def union(self, a, b):
        ra = self.find_root(a)
        rb = self.find_root(b)
        if ra != rb:
            self.t[max(ra, rb)] = min(ra, rb)

    def find_root(self, x):
        t = []
        while self.t[x] > 0:
            t.append(x)
            x = self.t[x]
        for _t in t:
            self.t[_t] = x
        return x


def solve(string):
    n, m, k, *abcd = map(int, string.split())
    ab, cd = abcd[:2 * m], abcd[2 * m:]
    r = [0] * (n + 1)
    uf = UnionFind(n)
    for a, b in zip(*[iter(ab)] * 2):
        r[a] += 1
        r[b] += 1
        uf.union(a, b)
    uf.flatten()
    for i, v in enumerate(uf.t):
        if v < 0:
            uf.t[i] = i
    mp = {k: [] for k in set(uf.t[1:])}
    for i, v in enumerate(uf.t[1:], start=1):
        mp[v].append(i)
    mp = {k: set(v) for k, v in mp.items()}
    for c, d in zip(*[iter(cd)] * 2):
        r[c] += 1 if d in mp[uf.t[c]] else 0
        r[d] += 1 if c in mp[uf.t[d]] else 0
    mp = {k: len(v) for k, v in mp.items()}
    return " ".join([str(mp[uf.t[i]] - 1 - r[i]) for i in range(1, n + 1)])


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
