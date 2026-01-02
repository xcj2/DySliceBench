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

    def sum(self, idx):
        res = 0
        while idx:
            res += self.tree[idx]
            idx -= idx & -idx
        return res

    def get(self, idx):
        return self.sum(idx) - self.sum(idx - 1)

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
        if res >= self.n:
            return self.n
        return res + 1

D = int(input())
C = list(map(int, input().split()))
S = [list(map(int, input().split())) for _ in range(D)]
T = [int(input()) for _ in range(D)]

M = int(input())
Q = [tuple(map(int, input().split())) for _ in range(M)]

res = 0
last = [0 for _ in range(26)]
used = [Set(list(range(D))) for i in range(26)]

for d in range(D):
    res += S[d][T[d] - 1]
    last[T[d] - 1] = d + 1
    used[T[d] - 1].insert(d)
    for j in range(26):
        res -= C[j] * ((d + 1) - last[j])

for i in range(M):
    d, q = Q[i]
    if T[d - 1] == q:
        print(res)
        continue
    res -= S[d - 1][T[d - 1] - 1]
    res += S[d - 1][q - 1]
    k = used[T[d - 1] - 1].sum(d - 1)
    l = used[T[d - 1] - 1].get(k - 1) if k != 1 else -1
    r = used[T[d - 1] - 1].get(k + 1)
    if r == 1000000000000000001:
        r = D
    res -= (d - 1 - l) * C[T[d - 1] - 1] * (r - d + 1)
    used[T[d - 1] - 1].delete(d - 1)
    used[q - 1].insert(d - 1)
    k = used[q - 1].sum(d - 1)
    l = used[q - 1].get(k - 1) if k != 1 else -1
    r = used[q - 1].get(k + 1)
    if r == 1000000000000000001:
        r = D
    res += (d - 1 - l) * C[q - 1] * (r - d + 1)
    T[d - 1] = q
    print(res)