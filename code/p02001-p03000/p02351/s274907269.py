class BinaryIndexedTree():  #1-indexed
    def __init__(self, n):
        self.n = n
        self.tree = [0 for _ in range(n + 1)]

    def sum(self, idx):
        res = 0
        while idx:
            res += self.tree[idx]
            idx -= idx & -idx
        return res

    def add(self, idx, x):
        while idx <= self.n:
            self.tree[idx] += x
            idx += idx & -idx

    def bisect_left(self, x):
        if x <= 0: return 0
        res, tmp = 0, 2**((self.n).bit_length() - 1)
        while tmp:
            if res + tmp <= self.n and self.tree[res + tmp] < x:
                x -= self.tree[res + tmp]
                res += tmp
            tmp >>= 1
        return res + 1

class RAQandRSQ():
    def __init__(self, n):
        self.bit1 = BinaryIndexedTree(n)
        self.bit2 = BinaryIndexedTree(n)

    def add(self, lt, rt, x):
        self.bit1.add(lt, -x * (lt - 1))
        self.bit1.add(rt, x * (rt - 1))
        self.bit2.add(lt, x)
        self.bit2.add(rt, -x)

    def sum(self, lt, rt):
        rsum = self.bit2.sum(rt - 1) * (rt - 1) + self.bit1.sum(rt - 1)
        lsum = self.bit2.sum(lt - 1) * (lt - 1) + self.bit1.sum(lt - 1)
        return rsum - lsum

import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

R = RAQandRSQ(N)

res = []

for _ in range(Q):
    q, *p = map(int, input().split())
    if q == 0:
        s, t, x = p
        R.add(s, t + 1, x)
    else:
        s, t = p
        res.append(R.sum(s, t + 1))

print('\n'.join(map(str, res)))
