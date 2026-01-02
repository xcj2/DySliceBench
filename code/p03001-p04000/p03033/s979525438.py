import sys
input = sys.stdin.readline
# Segment Tree
# segfunc : min, +, *, xor, gcd など
# identity_element : 単位元(min:inf, 和:0, 積:1, xor:0, gcd:0)


class Segment:
    def __init__(self, N, init_val):
        """[セグメント木]

        Args:
            N ([int]): [要素数]
            init_val ([list]): [初期化する値]
        """
        self.identity_element = 2 ** 31 - 1  # 変える
        self.N0 = 1 << (N - 1).bit_length()
        # 0-indexedで管理
        self.dat = [self.identity_element] * (2 * self.N0)
        # 値を代入
        for i in range(N):
            self.dat[i + self.N0 - 1] = init_val[i]
        # 構築
        for i in range(self.N0 - 2, -1, -1):
            self.dat[i] = self.segfunc(self.dat[2 * i + 1], self.dat[2 * i + 2])

    # k番目の要素の値をxに変更
    def update(self, k, x):
        k += self.N0 - 1
        self.dat[k] = x
        while k >= 0:
            k = (k - 1) // 2
            self.dat[k] = self.segfunc(self.dat[2 * k + 1], self.dat[2 * k + 2])

    # 区間[l,r)の最小値を求める
    def query(self, l, r):
        L = l + self.N0
        R = r + self.N0
        s = self.identity_element
        # 区間を列挙しながら最小値を求める
        while L < R:
            if R & 1:
                R -= 1
                s = self.segfunc(s, self.dat[R - 1])
            if L & 1:
                s = self.segfunc(s, self.dat[L - 1])
                L += 1
            L >>= 1
            R >>= 1
        return s

    def segfunc(self, x, y):
        return min(x, y)  # 変える


def compress(arr):
    *XS, = set(arr)
    XS.sort()
    return {e: i for i, e in enumerate(XS)}


n, q = map(int, input().split())
s, t, x = [0] * n, [0] * n, [0] * n
for i in range(n):
    s[i], t[i], x[i] = map(int, input().split())
    s[i] -= x[i]
    t[i] -= x[i]
    s[i] = max(s[i], 0)
    t[i] = max(t[i], 0)

d = [int(input()) for i in range(q)]

com = compress(s + t + d)
k = len(com) + 1

for i in range(n):
    s[i] = com[s[i]]
    t[i] = com[t[i]]

for i in range(q):
    d[i] = com[d[i]]
INF = 1 << 30
a = [INF] * k
b = [[] for i in range(k)]
c = [[] for i in range(k)]
seg = Segment(n, [INF] * n)
for i in range(n):
    b[s[i]].append(i)
    c[t[i]].append(i)

for i in range(k):
    for j in b[i]:
        seg.update(j, x[j])
    for j in c[i]:
        seg.update(j, INF)
    a[i] = seg.query(0, n)

for i in d:
    print(-1 if a[i] == INF else a[i])
