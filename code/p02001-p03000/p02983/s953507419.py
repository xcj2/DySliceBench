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
    l, r = input_ints()
    logging.debug([l, r])
    i_close = set()
    j_close = set()
    result = float('inf')
    for i in range(l, r):
        for j in range(i + 1, r + 1):
            result = min(result, (i * j) % 2019)
            j_close.add(j % 2019)
            if len(j_close) == 2019:
                break
        i_close.add(i % 2019)
        if len(i_close) == 2019:
            break
    print(result)


class Test(unittest.TestCase):
    def setUp(self):
        import run
        self._test = run

    def test_main(self):
        self._test.test_files(self, _main)


if __name__ == '__main__':
    _main()
