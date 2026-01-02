import typing
import sys

# import re
import math
import collections
# import decimal
import bisect
import itertools
import fractions
# import functools
import copy
import heapq
import decimal
# import statistics
import queue
# import numpy as np

# sys.setrecursionlimit(10000001)
INF = 10 ** 16
# MOD = 10 ** 9 + 7
MOD = 998244353


def ni(): return int(sys.stdin.readline())
def ns(): return map(int, sys.stdin.readline().split())
def na(): return list(map(int, sys.stdin.readline().split()))


# ===CODE===

# https://github.com/not522/ac-library-python#install


def _ceil_pow2(n: int) -> int:
    x = 0
    while (1 << x) < n:
        x += 1

    return x


class SegTree:
    def __init__(self,
                 # segtreeで実行したい関数
                 op: typing.Callable[[typing.Any, typing.Any], typing.Any],
                 # モノイド：op関数に入れたとしても絶対に相手側の値が変わらないことが保証されるような値(足し算なら0、maxなら-INFなど)
                 e: typing.Any,
                 # segtreeにしたい配列を初期生成して突っ込む方式
                 v: typing.Union[int, typing.List[typing.Any]]) -> None:
        self._op = op
        self._e = e

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = _ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)

        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    # st[p]にxを代入
    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    # st[p]を返す
    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        return self._d[p + self._size]

    # op(st[l],...,st[r-1])を返す　l==rのときはe()を返す
    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n
        sml = self._e
        smr = self._e
        left += self._size
        right += self._size

        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    # prod(0,len(a))のこと　l==rのときはe()を返す
    def all_prod(self) -> typing.Any:
        return self._d[1]

    # segtree上の二分探索 leftはベース fはleftより右側にあるst[left]に対して最初に条件を見たすindexを返す
    # 条件を満たすindexがないときはlen(a)が返ってくる
    # ex. segtree.max_right(x, lambda v: v < y) + 1  idx=xより右側にある最初のst[x]<st[v]となるvを返す()
    def max_right(self, left: int,
                  f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= left <= self._n
        assert f(self._e)

        if left == self._n:
            return self._n

        left += self._size
        sm = self._e

        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not f(self._op(sm, self._d[left])):
                while left < self._size:
                    left *= 2
                    if f(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    # segtree上の二分探索 rightはベース fはleftより左側にあるst[right]に対して最初に条件を見たすindexを返す
    # 条件を満たすindexがないときは0が返ってくる
    # ex. segtree.max_right(x, lambda v: v < y) + 1  idx=xより右側にある最初のst[x]<st[v]となるvを返す()
    def min_left(self, right: int,
                 f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= right <= self._n
        assert f(self._e)

        if right == 0:
            return 0

        right += self._size
        sm = self._e

        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not f(self._op(self._d[right], sm)):
                while right < self._size:
                    right = 2 * right + 1
                    if f(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])


def main():
    n, k = ns()
    a = [ni() for _ in range(n)]

    dp = [0 for _ in range(3*10**5+1)]

    st = SegTree(max, -1, dp)

    for ai in a:
        cnt = st.prod(max(0, ai-k), min(ai+k+1, 3*10**5+1))
        st.set(ai, cnt+1)
    ans = st.all_prod()
    print(ans)


if __name__ == '__main__':
    main()
