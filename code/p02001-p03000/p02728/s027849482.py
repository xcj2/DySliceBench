MOD = 1000000007
M = 2*10**5 + 10
fact = [1] * M
ifact = [1] * M
for i in range(2, M):
    fact[i] = fact[i - 1] * i % MOD
ifact[M - 1] = pow(fact[M - 1], MOD - 2, MOD)
for i in range(2, M - 1)[::-1]:
    ifact[i] = ifact[i + 1] * (i + 1) % MOD


def comb(n, k):
    if n < 0 or k > n:
        return 0
    return (fact[n] * ifact[k] % MOD) * ifact[n - k] % MOD


class DP:
    def __init__(self, dp = 1, size = 0):    
        self.dp = dp
        self.size = size

    def __add__(self, other):
        dp = self.dp
        dp *= other.dp
        dp %= MOD
        size = self.size + other.size
        dp *= comb(size, self.size)
        dp %= MOD
        return DP(dp, size)

    def __sub__(self, other):
        size = self.size - other.size
        dp = self.dp
        dp *= pow(comb(self.size, size), MOD - 2, MOD)
        dp %= MOD
        dp *= pow(other.dp, MOD - 2, MOD)
        dp %= MOD
        return DP(dp, size)

    def addRoot(self):
        return DP(self.dp, self.size + 1)


N = int(input())
e = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = [v - 1 for v in map(int, input().split())]
    e[a].append(b)
    e[b].append(a)

order = []
parent = [-1] * N
stack = [0]
while stack:
    v = stack.pop()
    order.append(v)
    for c in e[v]:
        if c == parent[v]:
             continue
        stack.append(c)
        parent[c] = v

dp = [DP() for _ in range(N)]
for v in order[1:][::-1]:
    dp[parent[v]] += dp[v].addRoot()
for v in order[1:]:
    d = dp[parent[v]] - dp[v].addRoot()
    dp[v] += d.addRoot()
for d in dp:
    print(d.dp)