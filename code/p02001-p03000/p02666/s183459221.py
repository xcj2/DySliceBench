import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()

class modfact(object):
    def __init__(self, n):
        fact, invfact = [1] * (n + 1), [1] * (n + 1)
        for i in range(1, n + 1): fact[i] = i * fact[i - 1] % MOD
        invfact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, -1, -1): invfact[i] = invfact[i + 1] * (i + 1) % MOD
        self._fact, self._invfact = fact, invfact

    def inv(self, n):
        return self._fact[n - 1] * self._invfact[n] % MOD

    def fact(self, n):
        return self._fact[n]

    def invfact(self, n):
        return self._invfact[n]

    def comb(self, n, k):
        if k < 0 or n < k: return 0
        return self._fact[n] * self._invfact[k] % MOD * self._invfact[n - k] % MOD

    def perm(self, n, k):
        if k < 0 or n < k: return 0
        return self._fact[n] * self._invfact[n - k] % MOD

class UnionFind(object):
    def __init__(self, n, recursion = False):
        self._par = list(range(n))
        self._size = [1] * n
        self._recursion = recursion

    def root(self, k):
        if self._recursion:
            if k == self._par[k]:
                return k
            self._par[k] = self.root(self._par[k])
            return self._par[k]
        else:
            root = k
            while root != self._par[root]: root = self._par[root]
            while k != root: k, self._par[k] = self._par[k], root
            return root

    def unite(self, i, j):
        i, j = self.root(i), self.root(j)
        if i == j: return False
        if self._size[i] < self._size[j]: i, j = j, i
        self._par[j] = i
        self._size[i] += self._size[j]
        return True

    def is_connected(self, i, j):
        return self.root(i) == self.root(j)

    def size(self, k):
        return self._size[self.root(k)]

def resolve():
    n = int(input())
    P = [a - 1 if a != -1 else -1 for a in map(int, input().split())]
    k = P.count(-1)

    E = [[] for _ in range(n)]
    for u, v in enumerate(P):
        if v != -1:
            E[u].append(v)
            E[v].append(u)

    # divide E into connected component
    color = [-1] * n
    cnt = 0
    def dfs(v):
        if color[v] != -1:
            return False
        color[v] = cnt
        stack = [v]
        while stack:
            v = stack.pop()
            for nv in E[v]:
                if color[nv] == -1:
                    color[nv] = cnt
                    stack.append(nv)
        return True
    for v in range(n):
        cnt += dfs(v)

    # detect loops for each color with union find
    has_loop = [False] * cnt
    uf = UnionFind(n)
    for v in range(n):
        nv = P[v]
        if nv == -1:
            continue
        if not uf.unite(v, nv):
            has_loop[color[v]] = True

    S = []
    for root in set(uf.root(v) for v in range(n)):
        if not has_loop[color[root]]:
            S.append(uf.size(root))

    ans = pow(n - 1, k, MOD) * (n - sum(has_loop))
    l = len(S)
    dp = [0] * (l + 1)
    dp[0] = 1
    for s in S:
        ndp = dp[:]
        for i in range(1, l + 1):
            ndp[i] += s * dp[i - 1]
            ndp[i] %= MOD
        dp = ndp

    # i >= 2
    mf = modfact(5001)
    for i in range(1, l + 1):
        if i == 1:
            ans -= sum(s - 1 for s in S) % MOD * pow(n - 1, k - 1, MOD)
        else:
            ans -= dp[i] * mf.fact(i - 1) % MOD * pow(n - 1, k - i, MOD)
        ans %= MOD

    print(ans)
resolve()