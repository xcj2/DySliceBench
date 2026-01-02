import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7


# MOD = 998244353

class BinaryIndexedTree:
    # http://hos.ac/slides/20140319_bit.pdf
    def __init__(self, size):
        """
        :param int size:
        """
        self._bit = [0] * size
        self._size = size

    def add(self, i, w):
        """
        i 番目に w を加える
        :param int i:
        :param int w:
        """
        x = i + 1
        while x <= self._size:
            self._bit[x - 1] += w
            x += x & -x

    def sum(self, i):
        """
        [0, i) の合計
        :param int i:
        """
        ret = 0
        while i > 0:
            ret += self._bit[i - 1]
            i -= i & -i
        return ret

    def __len__(self):
        return self._size


def argsort(li, key=None, reverse=False):
    return [i for _, i in sorted(
        [(a, i) for i, a in enumerate(li)], key=(lambda t: key(t[0])) if key else None, reverse=reverse
    )]


N, M, Q = list(map(int, sys.stdin.buffer.readline().split()))
LR = [list(map(int, sys.stdin.buffer.readline().split())) for _ in range(M)]
PQ = [list(map(int, sys.stdin.buffer.readline().split())) for _ in range(Q)]

LR.sort(reverse=True)
idx = argsort(PQ, reverse=True)
PQ.sort(reverse=True)

lri = 0
bit = BinaryIndexedTree(size=N + 1)
ans = [0] * Q
for i, (p, q) in enumerate(PQ):
    while lri < len(LR) and LR[lri][0] >= p:
        l, r = LR[lri]
        bit.add(r, 1)
        lri += 1
    ans[idx[i]] = bit.sum(q + 1)
print(*ans, sep='\n')
