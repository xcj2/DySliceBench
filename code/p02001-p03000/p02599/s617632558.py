import sys
input = sys.stdin.buffer.readline
from operator import itemgetter


class BIT:
    """一点加算、区間取得クエリをそれぞれO(logN)で答えるデータ構造"""
    def __init__(self, n):
        self.size = n
        self.bit = [0] * (n + 1)

    def build(self, array):
        """arrayを初期値とするBinaryIndexTreeを構築する O(N)"""
        for i in range(self.size):
            self.bit[i + 1] = array[i]
        for i in range(1, self.size):
            if i + (i & -i) > self.size:
                continue
            self.bit[i + (i & -i)] += self.bit[i]

    def _sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def add(self, i, val):
        """i番目の要素にvalを加える"""
        i += 1
        while i <= self.size:
            self.bit[i] += val
            i += i & -i

    def get_sum(self, l, r):
        """区間[l, r)の和を求める"""
        return self._sum(r) - self._sum(l)


n, q = map(int, input().split())
c = list(map(int, input().split()))
query = [list(map(int, input().split())) + [i] for i in range(q)]


bit = BIT(n)
memo = {}
ans = [0] * q
query = sorted(query, key=itemgetter(1))
ind = 0

for l, r, i in query:
    while ind < r:
        if c[ind] in memo:
            old_ind = memo[c[ind]]
        else:
            old_ind = -1
        memo[c[ind]] = ind
        bit.add(ind, 1)
        if old_ind != -1:
            bit.add(old_ind, -1)
        ind += 1
    ans[i] = bit.get_sum(l - 1, r)

print("\n".join(map(str, ans)))