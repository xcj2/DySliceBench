import collections
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
N = int(input())
S = list(input())
Q = int(input())
alpha = "abcdefghijklmnopqrstuvwxyz"
d = dict()

for x in alpha:
    d[x] = ord(x) - 97


class segment_tree:
    n = 0
    segtree = []

    def __init__(self, A):
        N = len(A)
        self.n = (N-1).bit_length()
        self.n = 1 << self.n
        self.segtree = [0 for i in range(2*self.n)]
        for i in range(N):
            self.segtree[self.n+i-1] = 1 << d[A[i]]
        for i in range(self.n - 2, -1, -1):
            self.segtree[i] = self.segtree[i*2 + 1] | self.segtree[i*2 + 2]

    def update(self, i, x):
        id = self.n+i - 1
        self.segtree[id] = 1 << d[x]
        while(id > 0):
            id = (id - 1) // 2
            self.segtree[id] = self.segtree[id *
                                            2 + 1] | self.segtree[id*2 + 2]

    def query(self, a, b, k, l, r):
        if r <= a or l >= b:
            return(0)
        if a <= l and r <= b:
            return(self.segtree[k])
        else:
            vl = self.query(a, b, k*2+1, l, (l+r)//2)
            vr = self.query(a, b, k*2+2, (l+r)//2, r)
            return(vl | vr)


def popcount(x):
    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f  # 8bitごと
    x = x + (x >> 8)  # 16bitごと
    x = x + (x >> 16)  # 32bitごと
    x = x + (x >> 32)  # 64bitごと = 全部の合計
    return x & 0x0000007f


ST = segment_tree(S[:-1])
N = (N-1).bit_length()
N = 1 << N

for _ in range(Q):
    t, a, b = input().split()

    if t == "1":
        a = int(a)
        ST.update(a-1, b)
    elif t == "2":
        a = int(a)
        b = int(b)
        ret = ST.query(a-1, b, 0, 0, N)
        print(popcount(ret))

    # print(ST.segtree)
