from collections import deque
import sys
input = sys.stdin.readline


class Combination:
    """階乗とその逆元のテーブルをO(N)で事前作成し、組み合わせの計算をO(1)で行う"""
    def __init__(self, n, MOD):
        self.fact = [1]
        for i in range(1, n + 1):
            self.fact.append(self.fact[-1] * i % MOD)
        self.inv_fact = [0] * (n + 1)
        self.inv_fact[n] = pow(self.fact[n], MOD - 2, MOD)
        for i in reversed(range(n)):
            self.inv_fact[i] = self.inv_fact[i + 1] * (i + 1) % MOD
        self.MOD = MOD

    def factorial(self, k):
        """k!を求める O(1)"""
        return self.fact[k]

    def inverse_factorial(self, k):
        """k!の逆元を求める O(1)"""
        return self.inv_fact[k]

    def permutation(self, k, r):
        """kPrを求める O(1)"""
        if k < r:
            return 0
        return (self.fact[k] * self.inv_fact[k - r]) % self.MOD

    def combination(self, k, r):
        """kCrを求める O(1)"""
        if k < r:
            return 0
        return (self.fact[k] * self.inv_fact[k - r] * self.inv_fact[r]) % self.MOD


def solve(tree, root):
    def dfs1():
        st1 = deque([root])
        st2 = deque([root])
        # 行きがけ順を記録
        while st1:
            v = st1.pop()
            for nxt_v in tree[v]:
                if nxt_v in par:
                    continue
                else:
                    par[nxt_v] = v
                    st1.append(nxt_v)
                    st2.append(nxt_v)
        # 帰りがけ順で処理
        while st2:
            v = st2.pop()
            res = 1
            c = 1
            for nxt_v in tree[v]:
                if nxt_v == par[v]:
                    continue
                else:
                    res *= dist1[nxt_v]
                    res *= comb.inv_fact[cnt[nxt_v]]
                    res %= MOD
                    c += cnt[nxt_v]
            cnt[v] = c
            dist1[v] = res * comb.fact[c - 1] % MOD
    def dfs2():
        q = deque([(root, 0, 0)])
        while q:
            v, par_val, par_cnt = q.pop()
            tmp_val = {}
            tmp_cnt = {}
            for nxt_v in tree[v]:
                if nxt_v == par[v]:
                    tmp_val[nxt_v] = par_val
                    tmp_cnt[nxt_v] = par_cnt
                else:
                    tmp_val[nxt_v] = dist1[nxt_v]
                    tmp_cnt[nxt_v] = cnt[nxt_v]
            res = 1
            c = 1
            for nxt_v in tmp_val:
                    res *= tmp_val[nxt_v]
                    res *= comb.inv_fact[tmp_cnt[nxt_v]]
                    res %= MOD
                    c += tmp_cnt[nxt_v]
            tmp_cnt[v] = c
            dist2[v] = res * comb.fact[c - 1] % MOD
            for nxt_v in tree[v]:
                if nxt_v == par[v]:
                    continue
                else:
                    tmp = dist2[v]\
                            * pow(tmp_val[nxt_v], MOD - 2, MOD) * comb.fact[tmp_cnt[nxt_v]] \
                            * comb.inv_fact[tmp_cnt[v] - 1] \
                            * comb.fact[tmp_cnt[v] - 1 - tmp_cnt[nxt_v]] % MOD
                    q.append((nxt_v, tmp, c - cnt[nxt_v]))

    par = {root: -1}
    dist1 = [0] * n
    cnt = [0] * n
    dist2 = [0] * n
    dfs1()
    dfs2()
    return dist2


n = int(input())
info = [list(map(int, input().split())) for i in range(n - 1)]
MOD = 10 ** 9 + 7

tree = [[] for i in range(n)]
for a, b in info:
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)

comb = Combination(10 ** 6, MOD)
for i in solve(tree, 0):
    print(i % MOD)