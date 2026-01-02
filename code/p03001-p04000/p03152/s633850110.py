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

MOD = 10**9 + 7

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

S = Set(list(range(N * M + 1)))
T = Set(list(range(N * M + 1)))

res = 1

for i in range(N):
    if S.count(A[i]):
        res = 0
    S.insert(A[i])

for i in range(M):
    if T.count(B[i]):
        res = 0
    T.insert(B[i])

for i in range(N * M):
    k = N * M - i
    if S.count(k) and T.count(k):
        res *= 1
    elif S.count(k):
        res *= T.sum(N * M) - T.sum(k)
    elif T.count(k):
        res *= S.sum(N * M) - S.sum(k)
    else:
        res *= (S.sum(N * M) - S.sum(k)) * (T.sum(N * M) - T.sum(k)) - i
    res %= MOD

print(res)