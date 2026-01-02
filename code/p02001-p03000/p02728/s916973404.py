class Combination:
    def __init__(self, size, mod=10**9 + 7):
        self.size = size + 2
        self.mod = mod
        self.fact = [1, 1] + [0] * size
        self.factInv = [1, 1] + [0] * size
        self.inv = [0, 1] + [0] * size

        for i in range(2, self.size):
            self.fact[i] = self.fact[i - 1] * i % self.mod
            self.inv[i] = -self.inv[self.mod % i] * (self.mod // i) % self.mod
            self.factInv[i] = self.factInv[i - 1] * self.inv[i] % self.mod

    def npr(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        return self.fact[n] * self.factInv[n - r] % self.mod

    def ncr(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        return self.fact[n] * (self.factInv[r] * self.factInv[n - r] % self.mod) % self.mod

    def nhr(self, n, r):  # 重複組合せ
        return self.ncr(n + r - 1, n - 1)

    def factN(self, n):
        if n < 0:
            return 0
        return self.fact[n]

class ReRooting:
    """
    0-indexed
    """
    def __init__(self, size, root=0, identDp=1, identCum=1):
        """
        identDp: 木DP用 lift(a, identDp) = a
        identCum: 累積用 merge(a, identCum) = a
        """
        self.size = size
        self.edges = [[] for _ in range(self.size + 1)]
        self.root = root
        self.identDp = identDp
        self.identCum = identCum

    def addEdge(self, fr, to):
        self.edges[fr].append(to)
        self.edges[to].append(fr)

    # 根を固定したときの木DP(貰うDP)
    def lift(self, top, bottom):
        newSize = top[1] + bottom[1] + 1
        dp = top[0] * bottom[0] * comb.ncr(newSize, bottom[1] + 1)
        return (dp % MOD, newSize)

    # 親の左右の累積から子を根としたときの値を求める
    def merge(self, left, right):
        newSize = left[1] + right[1]
        dp = left[0] * right[0] * comb.ncr(newSize, right[1])
        return (dp % MOD, newSize)

    def sol(self):
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
        for v in order[::-1]:  # 貰うDPしつつ，累積をとる
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
            dp[v] = self.lift(dp[v], fromParent[v])  # 最後に親からの貰うDP

        return dp[:N]

N = int(input())
MOD = 10**9 + 7
tree = ReRooting(N, 0, (1, -1), (1, 0))
comb = Combination(N + 100)

for _ in range(N - 1):
    fr, to = map(int, input().split())
    tree.addEdge(fr - 1, to - 1)

ans = tree.sol()
print(*[dp for dp, _ in ans[:N]], sep='\n')
