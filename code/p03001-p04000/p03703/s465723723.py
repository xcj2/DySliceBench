from bisect import bisect_left, bisect_right

class Set(): #BinaryIndexedTree
    def __init__(self, valuelist, INF=10**18+1):
        self.n = len(valuelist) + 1
        self.value = sorted(valuelist) + [INF]
        self.comp = {v : k for k, v in enumerate(self.value, 1)}
        self.bit = BinaryIndexedTree(self.n)

    def insert(self, x, k=1):
        self.bit.add(self.comp[x], k)

    def delete(self, x, k=1):
        self.bit.add(self.comp[x], -k)

    def count(self, x):
        return self.bit.get(self.comp[x])

    def sum(self, x):
        return self.bit.sum(self.comp[x])

    def get(self, k): #k個以下のときはINFを返す
        return self.value[self.bit.bisect_left(k) - 1]

class BinaryIndexedTree(): #1-indexed
    def __init__(self, n):
        self.n = n
        self.tree = [0 for _ in range(n + 1)]

    def sum(self, index):
        res = 0
        while index:
            res += self.tree[index]
            index -= index & -index
        return res

    def get(self, index):
        return self.sum(index) - self.sum(index - 1)

    def add(self, index, x):
        while index <= self.n:
            self.tree[index] += x
            index += index & -index

    def bisect_left(self, x):
        if x <= 0: return 0
        res, tmp = 0, 2**((self.n).bit_length() - 1)
        while tmp:
            if res + tmp <= self.n and self.tree[res + tmp] < x:
                x -= self.tree[res + tmp]
                res += tmp
            tmp >>= 1
        if res >= self.n:
            return self.n
        return res + 1

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

cum = [0]

for i in range(N):
    cum.append(cum[-1] + A[i])

V = [cum[i] - K * i for i in range(N + 1)]

S = Set(V)

res = 0

for i in range(N + 1):
    res += S.sum(V[i])
    S.insert(V[i])

print(res)