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
    fr, br = [[] for _ in range(n + 1)], [[] for _ in range(n + 1)]
    uf = UnionFind(n)
    for a, b in zip(*[iter(ab)] * 2):
        fr[a].append(b)
        fr[b].append(a)
        uf.union(a, b)
    uf.flatten()
    for i, v in enumerate(uf.t):
        if v < 0:
            uf.t[i] = i
    mp = {k: i for i, k in enumerate(set(uf.t[1:]))}
    g = [[] for _ in enumerate(mp.keys())]
    for i in range(n + 1):
        if uf.t[i] > 0:
            g[mp[uf.t[i]]].append(i)
    for c, d in zip(*[iter(cd)] * 2):
        br[c].append(d)
        br[d].append(c)

    *fr, = map(len, fr)
    *g, = map(set, g)
    *gn, = map(len, g)
    return " ".join([
        str(gn[mp[uf.t[i]]] - 1 - fr[i] - sum(j in g[mp[uf.t[i]]]
                                              for j in br[i]))
        for i in range(1, n + 1)
    ])


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
