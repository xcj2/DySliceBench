# range set query
from collections import defaultdict
import sys


def input(): return sys.stdin.readline().rstrip()


class BIT():
    # 1,,,,,,,Nまでの数値を扱える
    def __init__(self, n):
        self.n = n
        self.data = [0]*(n+1)

    def to_sum(self, i):
        # i番目のところまでのΣ
        s = 0
        while i > 0:
            s += self.data[i]
            i -= (i & -i)
        return s

    def add(self, i, x):
        # i 番目のところに+
        while i <= self.n:
            self.data[i] += x
            i += (i & -i)

    def get(self, i, j):
        # i番目からj番目までの要素のΣ(1<=i<=j<=Nという制約)
        return self.to_sum(j)-self.to_sum(i-1)


que = []
color_data = defaultdict(list)

N, Q = map(int, input().split())
C = list(map(int, input().split()))

for i in range(Q):
    l, r = map(int, input().split())
    que.append((i, l, r))

que.sort(key=lambda x: x[-1])

ans = [-1]*(Q)
previous_color = [-1]*(N+1)

for i, v in enumerate(C):
    color_data[v].append(i+1)

for key in color_data.keys():
    D = color_data[key]
    for i in range(1, len(D)):
        previous_color[D[i]] = D[i-1]

bit_tree = BIT(N)
i0, l0, r0 = que[0]

for _ in range(1, r0+1):
    bit_tree.add(_, 1)
    prev = previous_color[_]
    if prev > 0:
        bit_tree.add(prev, -1)
    ans[i0] = bit_tree.get(l0, r0)

for _ in range(1, Q):
    i, l, r = que[_]
    prv_r = que[_-1][-1]
    for j in range(prv_r+1, r+1):
        bit_tree.add(j, 1)
        prev = previous_color[j]
        if prev > 0:
            bit_tree.add(prev, -1)
    ans[i] = bit_tree.get(l, r)

for x in ans:
    print(x)