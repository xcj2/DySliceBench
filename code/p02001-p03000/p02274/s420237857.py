n = int(input())
a = list(map(int,input().split()))

from collections import defaultdict

class BIT:
    # 1-indexedに注意！
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
 
# 使用例
# bit = BIT(10)     # 要素数を与えてインスタンス化
# bit.add(2, 10)    # a2に10を加える
# bit.add(5, 5)     # a5に 5を加える
# print(bit.sum(3)) # a1～a3の合計を返す => 10
# print(bit.sum(6)) # a1～a6の合計を返す => 15
# bit.add(3, -6)    # a3に-6を加える
# print(bit.sum(6)) # a1～a6の合計を返す => 9
# print(bit.sum(6) - bit.sum(3))  # a4～a6の合計 => 5
# bit.add(10,7)     # a10に7を加える
# print(bit.sum(10))# a1〜a10の合計を返す => 16

bit = BIT(n)

b = sorted(a)
# print(b)

d = defaultdict(int)
for i in range(n):
    d[b[i]] = i
# print(list(d))

ans = 0
for i in range(n):
    t = a[i]
    ind = d[t] + 1
    ans += i - bit.sum(ind)
    bit.add(ind,1)

print(ans)
