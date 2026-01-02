#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
INF = float("inf")

MOD = 1000000007  # type: int


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def main():
    N = int(input())
    P = list(map(int, input().split()))

    # 確定している道でグルーピングする
    uf = UnionFind(N)
    K = 0
    undef = []                  # 要請未完ノードは記録
    for i, p in enumerate(P):
        if p != -1:
            uf.union(i, p-1)
        else:
            K += 1
            undef.append(i)

    # 階乗の事前計算
    factorial = [1]*K
    for i in range(K-1):
        factorial[i+1] = ((i+1)*factorial[i]) % MOD

    # 要請が未完のノードが属するグループサイズをメモ
    size_undef = []
    for u in undef:
        size_undef.append(uf.size(u))

    # dp[i, j]: i個の根付き木を見てj個を選んだ時の\sum{\prod_v S_v}
    # 「メモリ削減したdpとN^2確保するDP、どっちが早いんやろなあ」
    dp = [0]*(K+1)
    dp[0] = 1
    dp_new = dp[:]
    for i in range(1, K+1):
        for j in range(i):
            dp_new[j+1] += dp[j]*size_undef[i-1]
        dp = dp_new[:]

    # ただしj=1個を選んだ時のものは特別にsize[i]-1を考える必要がある
    if K >= 1:
        tot = 0
        for s in size_undef:
            tot += s-1
        dp[1] = tot

    # cycleをカウントする
    cycle_count = 0
    for i in range(1, K+1):
        # i個のグループからなるサイクルがひとつできる
        buf = dp[i]*factorial[i-1]
        buf %= MOD
        buf *= pow(N-1, K-i, MOD)
        buf %= MOD
        cycle_count += buf

    # すでに固定サイクルがあれば数える
    cycle_count += (uf.group_count()-K)*pow(N-1, K, MOD)

    # 求めます
    ans = N*pow(N-1, K, MOD) - cycle_count
    ans %= MOD

    print(ans)

    return


if __name__ == '__main__':
    main()
