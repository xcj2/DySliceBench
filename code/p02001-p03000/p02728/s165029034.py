class ReRooting:
    def __init__(self, size, root, identDp=0, identCum=0):
        self.size = size
        self.edges = [[] for _ in range(self.size + 1)]
        self.root = root
        self.identDp = identDp
        self.identCum = identCum

    def addEdge(self, fr, to):
        self.edges[fr].append(to)
        self.edges[to].append(fr)

    # 根を固定したときの木DP
    def lift(self, top, bottom):
        return (((top[0] * bottom[0]) % MOD * comb.ncr(top[1] + bottom[1] + 1, top[1])) % MOD, top[1] + bottom[1] + 1)

    # 子の累積
    def merge(self, cum, a):
        return (((cum[0] * a[0]) % MOD * comb.ncr(cum[1] + a[1], cum[1])) % MOD, cum[1] + a[1])

    def sol(self):
        # 普通に木DPをする
        # 並行して各頂点につき、子の値の累積liftを左右から求めておく
        # その後根から順番に、親からの寄与を求めていく(fromParent)
        N = self.size
        edges = self.edges

        st = [self.root]
        parent = [-1] * (N + 1)
        child = [[] for _ in range(N + 1)]
        order = []
        while st:
            v = st.pop()
            order.append(v)
            for to in edges[v]:
                if parent[v] == to:
                    continue
                parent[to] = v
                child[v].append(to)
                st.append(to)

        dp = [self.identDp] * (N + 1)
        left = [self.identCum] * (N + 1)
        right = [self.identCum] * (N + 1)
        for v in order[::-1]:
            tmp = self.identCum
            for ch in child[v]:
                left[ch] = tmp
                tmp = self.lift(tmp, dp[ch])
            tmp = self.identCum
            for ch in reversed(child[v]):
                right[ch] = tmp
                tmp = self.lift(tmp, dp[ch])
            dp[v] = tmp

        fromParent = [self.identDp] * (N + 1)
        for v in order:
            if v == self.root:
                continue
            fromParent[v] = self.lift(self.merge(left[v], right[v]), fromParent[parent[v]])
            dp[v] = self.lift(dp[v], fromParent[v])

        return dp[:N]

class Combination:
    def __init__(self, size, MOD=10**9 + 7):
        self.size = size + 2
        self.MOD = MOD
        self.fact = [1, 1] + [0] * size
        self.factInv = [1, 1] + [0] * size
        self.inv = [0, 1] + [0] * size

        for i in range(2, self.size):
            self.fact[i] = self.fact[i - 1] * i % self.MOD
            self.inv[i] = -self.inv[self.MOD % i] * (self.MOD // i) % self.MOD
            self.factInv[i] = self.factInv[i - 1] * self.inv[i] % self.MOD

    def npr(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        return self.fact[n] * self.factInv[n - r] % self.MOD

    def ncr(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        return self.fact[n] * (self.factInv[r] * self.factInv[n - r] % self.MOD) % self.MOD

    def nhr(self, n, r):  # 重複組合せ
        return self.ncr(n + r - 1, n - 1)

    def factN(self, n):
        if n < 0:
            return 0
        return self.fact[n]

N = int(input())
MOD = 10**9 + 7
comb = Combination(2 * 10**5 + 100)

tree = ReRooting(N, 0, (1, -1), (1, 0))

for _ in range(N - 1):
    fr, to = map(int, input().split())
    tree.addEdge(fr - 1, to - 1)

ans = tree.sol()
print(*[a for a, b in ans], sep='\n')