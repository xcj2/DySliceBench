"""
sum{j} - sum(i) >= K(j - i)
sum{j} - Ki >= sum(i) - Ki
"""

n,k = map(int,input().split())

al = []

for _ in range(n):
    a = int(input())
    al.append(a)

import itertools
al_ac = [0] + list(itertools.accumulate(al))

for i in range(n+1):
    al_ac[i] -= i * k

# 入力: 座標の配列
# 出力 MP[e] = i: 座標eはi番目に該当
def compress(arr):
    *XS, = set(arr)
    XS.sort()
    return {e: i for i, e in enumerate(XS)}

dic = compress(al_ac)
bl = [dic[b] for b in al_ac]
k = max(bl)

# Binary Indexed Tree (Fenwick Tree)
class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0]*(n+1)
        self.el = [0]*(n+1)
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s
    def add(self, i, x):
        # assert i > 0
        self.el[i] += x
        while i <= self.n:
            self.data[i] += x
            i += i & -i
    def get(self, i, j=None):
        if j is None:
            return self.el[i]
        return self.sum(j) - self.sum(i)


ans = 0
bit = BIT(k+2)
for b in bl:
    ans += bit.sum(b+1)
    bit.add(b+1, 1)

print(ans)