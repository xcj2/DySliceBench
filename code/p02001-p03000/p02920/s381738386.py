import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7


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


def compress(li, origin=0):
    """
    座圧
    :param li:
    :param int origin:
    :rtype: list of int
    """
    *ret, = map({v: i + origin for i, v in enumerate(sorted(set(li)))}.__getitem__, li)
    return ret


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


N = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))


def solve(S):
    S = compress(S, origin=1)
    S.sort(reverse=True)

    # bit[i]: サイズが i 以下のスライムの数
    bit = BinaryIndexedTree(size=max(S) + 1)
    for s in S:
        bit.add(s, 1)

    slimes = [S[0]]
    bit.add(S[0], -1)

    for _ in range(N):
        cnt = len(slimes)
        for i in range(cnt):
            # slimes[i] より小さい、一番大きいスライムを作る
            smallers = bit.sum(slimes[i] - 1)
            if smallers == 0:
                return False
            # 作れたら1減らす
            s = bisect_left_callable(bit.sum, smallers, lo=0, hi=slimes[i])
            slimes.append(s)
            bit.add(s, -1)
    return True


if solve(S):
    print('Yes')
else:
    print('No')
