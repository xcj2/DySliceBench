class DisjointSetUnion():
    def __init__(self, n):
        self.n = n
        self.par_size = [-1] * n

    def merge(self, a, b):
        #assert 0 <= a < self.n
        #assert 0 <= b < self.n
        x = self.leader(a)
        y = self.leader(b)
        if x == y: return x
        if -self.par_size[x] < -self.par_size[y]: x, y = y, x
        self.par_size[x] += self.par_size[y]
        self.par_size[y] = x
        return x

    def same(self, a, b):
        #assert 0 <= a < self.n
        #assert 0 <= b < self.n
        return self.leader(a) == self.leader(b)

    def leader(self, a):
        #assert 0 <= a < self.n
        x = a
        while self.par_size[x] >= 0:
            x = self.par_size[x]
        while self.par_size[a] >= 0:
            self.par_size[a] = x
            a = self.par_size[a]
        return x

    def size(self, a):
        #assert 0 <= a < self.n
        return -self.par_size[self.leader(a)]

    def groups(self):
        leader_buf = [0] * self.n
        group_size = [0] * self.n
        res = [[] for _ in range(self.n)]
        for i in range(self.n):
            leader_buf[i] = self.leader(i)
            group_size[leader_buf[i]] += 1
        for i in range(self.n):
            res[leader_buf[i]].append(i)
        res = [res[i] for i in range(self.n) if res[i]]
        return res

class BinaryIndexedTree():  #0-indexed
    def __init__(self, n):
        self.n = n
        self.tree = [0 for _ in range(n + 1)]

    def sum(self, idx):
        res = 0
        idx += 1
        while idx:
            res += self.tree[idx]
            idx -= idx & -idx
        return res

    def add(self, idx, x):
        idx += 1
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
        return res



N = int(input())
T = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(N)]

uf = DisjointSetUnion(N)

#x座標 -> 辺のid
X = [0] * N

#y座標 -> 辺のid
Y = [0] * N

for i in range(N):
    x, y = T[i]
    X[x] = i
    Y[y] = i

bit1 = BinaryIndexedTree(N)

#x座標の小さいものからみていく
#T[X[i]][0] いまみているx座標 = i
#T[X[i]][1] いまみているy座標

for i in range(N):
    #これまで見た中で自分よりも小さなY座標のものがあるか判定する その中で一番大きなものを選ぶ
    sm = bit1.sum(T[X[i]][1])
    s = bit1.bisect_left(sm)
    if sm > 0 and s < T[X[i]][1]:
        uf.merge(Y[s], X[i]) #Y座標がsであるものとX座標がiであるものはペアになれる
    s = bit1.bisect_left(1)
    if s < T[X[i]][1]:
        uf.merge(Y[s], X[i])
    bit1.add(T[X[i]][1], 1) #いまみているY座標に+1

R = []

for i in range(N):
    x, y = T[i]
    R.append((N - 1 - x, N - 1 - y))

X2 = [0] * N
Y2 = [0] * N

for i in range(N):
    x, y = R[i]
    X2[x] = i
    Y2[y] = i

bit2 = BinaryIndexedTree(N)

for i in range(N):
    sm = bit2.sum(R[X2[i]][1])
    s = bit2.bisect_left(sm)
    if sm > 0 and s < R[X2[i]][1]:
        uf.merge(Y2[s], X2[i])
    s = bit2.bisect_left(1)
    if s < R[X2[i]][1]:
        uf.merge(Y2[s], X2[i])
    bit2.add(R[X2[i]][1], 1)

res = []

for i in range(N):
    res.append(uf.size(i))

print('\n'.join(map(str, res)))