import itertools
import math
import os
import sys
from collections import defaultdict
from operator import itemgetter

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7


class SparseTable:
    """
    構築 O(NlogN)、クエリ O(1)
    """

    def __init__(self, values, fn):
        """
        :param list values:
        :param callable fn: 結合則を満たす冪等な関数。min、max など。add はだめ
        """
        self._values = values
        self._fn = fn

        # SparseTable を構築
        # self._table[i][p]: [i, i+2^p) に fn を適用した結果の値のインデックス
        self._table = self._build(values, fn)

        # self._msb[i]: 最上位ビット; どの p を見るべきか
        self._msb = [0] * (len(values) + 1)
        for i in range(2, len(values) + 1):
            self._msb[i] = self._msb[i >> 1] + 1

    @staticmethod
    def _build(values, fn):
        # AtCoder の PyPy 2.4.0 では math.log2 が使えない
        size = int(math.log(len(values), 2)) + 1

        st = [[0] * size for _ in range(len(values))]
        for i in range(len(values)):
            st[i][0] = i
        for p in range(1, size):
            for i in range(len(values)):
                q = min(i + (1 << (p - 1)), len(values) - 1)
                l = st[i][p - 1]
                r = st[q][p - 1]
                if values[l] == fn(values[l], values[r]):
                    st[i][p] = l
                else:
                    st[i][p] = r
        return st

    def get(self, a, b):
        """
        半開区間 [a, b) に fn を適用した結果
        :param int a:
        :param int b:
        """
        if b <= a:
            return None
        p = self._msb[b - a]
        return self._fn(
            self._values[self._table[a][p]],
            self._values[self._table[b - (1 << p)][p]]
        )


N = int(sys.stdin.readline())
LR = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def calc_score(lr):
    ma = IINF
    mi = 0
    for l, r in lr:
        ma = min(ma, r)
        mi = max(mi, l)
    return max(0, ma - mi + 1)


def test(N, LR):
    import numpy as np
    LR = np.array(LR, dtype=int)
    ret = 0
    counts = defaultdict(int)
    for choice in itertools.product([True, False], repeat=N):
        if sum(choice) in [N, 0]:
            continue
        choice = np.array(choice)
        score = calc_score(LR[choice]) + calc_score(LR[~choice])
        if score >= ret:
            counts[score] = max(counts[score], sum(choice))
        ret = max(score, ret)
        # print(score, choice)
    # print(ret, counts[ret])
    return ret


def argsort(li, key=None, reverse=False):
    return [i for _, i in sorted([(a, i) for i, a in enumerate(li)], key=(lambda t: key(t[0])) if key else None, reverse=reverse)]


def solve():
    L, R = zip(*LR)
    L = list(L)
    R = list(R)
    if N == 2:
        ans = R[0] - L[0] + 1 + R[1] - L[1] + 1
        # ans = (R - L + 1).sum()
        print(ans)
        exit()

    # minR と minL のやつを同じグループにするとき、一番幅が広いのを他のグループにするのが最適。
    diff = [r - l for r, l in zip(R, L)]
    order = argsort(diff)
    L = [L[o] for o in order]
    R = [R[o] for o in order]
    diff.sort()
    li = L.index(max(L))
    ri = R.index(min(R))

    g1i = N - 1
    while g1i in [li, ri]:
        g1i -= 1
    g1 = diff[g1i] + 1
    g2 = max(0, R[ri] - L[li] + 1)
    ans1 = g1 + g2

    # minR と minL のやつを違うグループにするとき、どこで区切るかを全探索。
    LR.sort()
    L, R = zip(*LR)
    rsp = SparseTable(R, min)
    ans2 = 0
    for sep in range(1, N):
        max_l = L[sep - 1]
        min_r = rsp.get(0, sep)
        s1 = max(0, min_r - max_l + 1)
        max_l = L[-1]
        min_r = rsp.get(sep, N)
        s2 = max(0, min_r - max_l + 1)
        score = s1 + s2
        ans2 = max(score, ans2)

    LR.sort(key=itemgetter(1))
    L, R = zip(*LR)
    lsp = SparseTable(L, max)
    for sep in range(1, N):
        max_l = lsp.get(0, sep)
        min_r = R[0]
        s1 = max(0, min_r - max_l + 1)
        max_l = lsp.get(sep, N)
        min_r = R[sep]
        s2 = max(0, min_r - max_l + 1)
        score = s1 + s2
        ans2 = max(score, ans2)

    return max(ans1, ans2)


print(solve())
# assert test(N, LR) == solve()
