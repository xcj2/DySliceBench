import itertools
import os
import sys
from collections import defaultdict

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
N += 1
P = [0] + P

def test(A):
    N = len(A)
    ret = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            b = A[i: j + 1].copy()
            b.sort()
            ret += b[-2]
    return ret


#
# ans = defaultdict(list)
# for a in itertools.permutations(range(1, 5)):
#     t = test(list(a))
#     ans[t].append(a)
#
# for k in sorted(ans.keys()):
#     print('--- {} ---'.format(k))
#     for v in ans[k]:
#         print(v)


# ans = test(P)
# print(ans)


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
        :return:
        """
        x = i + 1
        while x <= self._size:
            self._bit[x - 1] += w
            x += x & -x

    def sum(self, i):
        """
        0 番目から i 番目までの合計
        :param int i:
        :return:
        """
        ret = 0
        x = i + 1
        while x > 0:
            ret += self._bit[x - 1]
            x -= x & -x
        return ret

    def __len__(self):
        return self._size


def bisect_left_callable(fn, x, lo, hi):
    """
    :param callable fn:
    :param x:
    :param int lo: 最小値
    :param int hi: 最大値 + 1
    :return: lo <= ret <= hi
    """
    while lo < hi:
        mid = (lo + hi) // 2
        if fn(mid) < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def argsort(li):
    return [i for _, i in sorted([(a, i) for i, a in enumerate(li)], reverse=True)]


bit = BinaryIndexedTree(size=N)

idx = argsort(P)
ans = 0
for i in idx[:-1]:
    cnt = bit.sum(i)
    # cnt が 1 減る場所
    l1 = bisect_left_callable(lambda k: bit.sum(k), cnt, lo=0, hi=i)
    l2 = bisect_left_callable(lambda k: bit.sum(k), cnt - 1, lo=0, hi=i)
    # 1 増える場所
    r1 = bisect_left_callable(lambda k: bit.sum(k), cnt + 1, lo=i + 1, hi=N)
    r2 = bisect_left_callable(lambda k: bit.sum(k), cnt + 2, lo=i + 1, hi=N)

    a = (r1 - i) * (l1 - l2)
    b = (i - l1) * (r2 - r1)
    # print(P[i], l1, l2, r1, r2, a, b)
    # print(P[i], a + b)

    ans += P[i] * (a + b)
    bit.add(i, 1)
print(ans)
