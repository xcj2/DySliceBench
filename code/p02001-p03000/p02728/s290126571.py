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


class rerooting:
    def __init__(self, tree):
        self.tree = tree
        self.root = 0
        self.n = len(tree)
        self.par = {self.root: -1}
        self.e = (1, 1)
        self.val1 = [self.e for _ in range(self.n)]
        self.val2 = [self.e for _ in range(self.n)]
        self._dfs1()
        self._dfs2()

    def node_merge(self, sub, node):
        ptn_sub, cnt_sub = sub
        ptn_node, cnt_node = node
        cnt = cnt_sub + cnt_node
        return (ptn_sub * ptn_node * comb.combination(cnt - 1, cnt_node) % MOD, cnt)
      
    def node_purge(self, sub, node):
        ptn_sub, cnt_sub = sub
        ptn_node, cnt_node = node
        inv_ptn_node = pow(ptn_node, MOD - 2, MOD)
        inv_comb = pow(comb.combination(cnt_sub - 1, cnt_node), MOD - 2, MOD)
        inv_cnt = cnt_sub - cnt_node
        return (ptn_sub * inv_ptn_node * inv_comb % MOD, inv_cnt)
         
    def _dfs1(self):
        st1, st2 = deque([self.root]), deque([self.root])
        # 行きがけ順を記録
        while st1:
            v = st1.pop()
            for nxt_v in self.tree[v]:
                if nxt_v in self.par:
                    continue
                else:
                    self.par[nxt_v] = v
                    st1.append(nxt_v)
                    st2.append(nxt_v)
        # 帰りがけ順で処理
        while st2:
            v = st2.pop()
            for nxt_v in self.tree[v]:
                if nxt_v == self.par[v]:
                    continue
                else:
                    self.val1[v] = self.node_merge(self.val1[v], self.val1[nxt_v])

    def _dfs2(self):
        q = deque([(self.root, self.e)])
        while q:
            v, par_val = q.pop()
            tmp = {}
            for nxt_v in self.tree[v]:
                if nxt_v == self.par[v]:
                    tmp[nxt_v] = par_val
                else:
                    tmp[nxt_v] = self.val1[nxt_v]
            for nxt_v in tmp:
                self.val2[v] = self.node_merge(self.val2[v], tmp[nxt_v])

            for nxt_v in tree[v]:
                if nxt_v == self.par[v]:
                    continue
                else:
                    q.append((nxt_v, self.node_purge(self.val2[v], self.val1[nxt_v])))


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
rt = rerooting(tree)
for i in range(n):
    print(rt.val2[i][0])