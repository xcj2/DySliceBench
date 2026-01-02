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


N = int(sys.stdin.buffer.readline())
A = list(map(int, sys.stdin.buffer.readline().split()))
N += 1

if N == 1:
    if A[0] == 1:
        print(1)
    else:
        print(-1)
    exit()

# # TODO: 繰り返しをなくす
# def test():
#     d = 0
#     ok = True
#     for i in range(N):
#         for _ in range(A[i]):
#             # i より前で cap が 0 以上で一番前のところから取る
#             if d > i:
#                 ok = False
#                 break
#             cap[d] -= 1
#             cap[d + 1:i] += 1
#             counts[d + 1: i + 1] += 1
#             while d < len(cap) and d < 70 and cap[d] <= 0:
#                 d += 1
#         print(counts, cap, d, ok)
#     print(counts.sum())
#     return counts.sum()


# cap = np.ones(N, dtype=int)
# cap[-1] = 0
# # counts = [1] * N
# counts = np.ones(N, dtype=int)


bit = BinaryIndexedTree(size=N + 10)
bit.add(0, 1)
bit.add(N - 1, -1)
A[-1] -= 1

d = 0
ok = True
ans = N
for i in range(N):
    while A[i] > 0:
        # i より前で cap が 0 以上で一番前のところから取る
        if d >= i:
            ok = False
            break
        # a = min(A[i], cap[d])
        a = min(A[i], bit.sum(d + 1))
        A[i] -= a

        # cap[d] -= a
        bit.add(d, -a)
        bit.add(d + 1, a)
        # cap[d + 1:i] += a
        bit.add(d + 1, a)
        bit.add(i, -a)

        # counts[d + 1: i + 1] += a
        ans += a * (i - d)
        while d < N and bit.sum(d + 1) <= 0:
            d += 1

    if not ok:
        break
    # for i in range(len(bit)):
    #     print(bit.sum(i + 1), end=' ')
    # print()
    # print(counts, cap, d, ok)
    # print()
if ok:
    print(ans)
else:
    print(-1)
exit()
# print(counts.sum(), ans)
# test()
