import sys
from collections import defaultdict


class SegTree:
    def __init__(self, n, s):
        """
        :param n: 要素数
        :param INF: 初期値（入りうる要素より十分に大きな数）
        """
        n2 = 1 << (n - 1).bit_length()
        self.offset = n2
        self.tree = [None] * n2 + [{} for _ in range(n2)]
        self.lmd0 = lambda: 0

        for i, c in enumerate(s):
            x = ord(c) - 97
            i += self.offset
            self.tree[i][x] = 1
        for i in range(self.offset - 1, 0, -1):
            sti = self.tree[i] = defaultdict(self.lmd0, self.tree[i << 1])
            stj = self.tree[(i << 1) + 1]
            for x in stj:
                sti[x] += stj[x]
        # print(*(dict(t) for t in self.tree), sep='\n')

    def update(self, i, x):
        """
        i番目の値をxに更新
        :param i: index(0-indexed)
        :param x: update value
        """
        i += self.offset
        if x in self.tree[i]:
            return
        y, _ = self.tree[i].popitem()
        self.tree[i][x] = 1
        i >>= 1
        while i > 0:
            sti = self.tree[i]
            sti[x] += 1
            if sti[y] == 1:
                del sti[y]
            else:
                sti[y] -= 1
            i >>= 1

    def get_types(self, a, b):
        """
        [a, b)の最小値を得る
        :param a: index(0-indexed)
        :param b: index(0-indexed)
        """
        result = set()

        l = a + self.offset
        r = b + self.offset
        while l < r:
            if r & 1:
                result.update(self.tree[r - 1].keys())
            if l & 1:
                result.update(self.tree[l].keys())
                l += 1
            l >>= 1
            r >>= 1

        return len(result)


n = int(input())
s = input()
st = SegTree(n, s)
q = int(input())
ans = []
for line in sys.stdin:
    i, j, k = line.rstrip().split()
    if i == '1':
        j = int(j) - 1
        k = ord(k) - 97
        st.update(j, k)
    else:
        l = int(j) - 1
        r = int(k)
        ans.append(st.get_types(l, r))
print('\n'.join(map(str, ans)))
