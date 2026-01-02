import types

_atcoder_code = """
# Python port of AtCoder Library.

__version__ = '0.0.1'
"""

atcoder = types.ModuleType('atcoder')
exec(_atcoder_code, atcoder.__dict__)

_atcoder__bit_code = """
def _ceil_pow2(n: int) -> int:
    x = 0
    while (1 << x) < n:
        x += 1

    return x


def _bsf(n: int) -> int:
    x = 0
    while n % 2 == 0:
        x += 1
        n //= 2

    return x
"""

atcoder._bit = types.ModuleType('atcoder._bit')
exec(_atcoder__bit_code, atcoder._bit.__dict__)


_atcoder_segtree_code = """
import typing

# import atcoder._bit


class SegTree:
    def __init__(self,
                 op: typing.Callable[[typing.Any, typing.Any], typing.Any],
                 e: typing.Any,
                 v: typing.Union[int, typing.List[typing.Any]]) -> None:
        self._op = op
        self._e = e

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = atcoder._bit._ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)

        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        return self._d[p + self._size]

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

    def all_prod(self) -> typing.Any:
        return self._d[1]

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
"""

atcoder.segtree = types.ModuleType('atcoder.segtree')
atcoder.segtree.__dict__['atcoder'] = atcoder
atcoder.segtree.__dict__['atcoder._bit'] = atcoder._bit
exec(_atcoder_segtree_code, atcoder.segtree.__dict__)
SegTree = atcoder.segtree.SegTree

import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# from atcoder.fenwicktree import FenwickTree

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


import typing


# from atcoder.segtree import SegTree

LARGE = 3*10**5

def solve(arr, k):  # fix inputs here
    console("----- solving ------")
    console(arr,k)

    segtree = SegTree(max, -1, LARGE+2)

    maxres = 0

    for a in arr:
        maxval = 0

        maxsmall = max(0, a - k)
        minlarge = min(LARGE, a + k) + 1
        maxval = max(maxval, segtree.prod(maxsmall, minlarge))

        maxval += 1
        maxres = max(maxres, maxval)

        console(a, maxsmall, minlarge, maxval, maxres)
        segtree.set(a, maxval)

    return maxres




def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
inp = sys.stdin.readlines()

for case_num in [1]:
    # read line as a string
    # strr = input()

    # read line as an integer
    # nrows = int(inp[0])
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    nrows, k = list(map(int,inp[0].split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid = []
    for n in range(nrows):
        grid.append(list(map(int,inp[n+1].split()))[0])

    res = solve(grid, k)  # please change
    
    # res = "\n".join(str(x) for x in res)
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
