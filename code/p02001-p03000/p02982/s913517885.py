import functools as ft
import heapq
import itertools as it
import logging
import unittest
from collections import (
    OrderedDict,
    defaultdict,
    namedtuple,
    Counter,
)

import numpy as np

_ = [ft, it, np, heapq, namedtuple, Counter, defaultdict, OrderedDict]

debug = logging.getLogger(__name__).debug


def input_ints():
    return list(map(int, input().strip().split()))


def _main():
    n, d = input_ints()
    x = [input_ints() for _ in range(n)]
    x = np.array(x)
    print(sum(
        d == np.round(d)
        for i in range(n)
        for j in range(i)
        for d in [np.sqrt(np.sum((x[i] - x[j]) ** 2))]
    ))


class Test(unittest.TestCase):
    def setUp(self):
        import run
        self._test = run

    def test_main(self):
        self._test.test_files(self, _main)


if __name__ == '__main__':
    _main()
