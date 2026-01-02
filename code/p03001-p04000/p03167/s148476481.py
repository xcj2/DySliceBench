#!/usr/bin/env python3
# vim: set fileencoding=utf-8

# pylint: disable=unused-import, invalid-name, missing-docstring, bad-continuation


"""Module docstring
"""

import functools
import heapq
import itertools
import logging
import math
import random
import string
import sys
from argparse import ArgumentParser
from collections import defaultdict, deque
from copy import deepcopy

MODULO = pow(10, 9) + 7


def solve(values, h, w):
    dp = [[0] * (1 + w) for _ in range(1 + h)]
    dp[1][1] = 1
    for i in range(h):
        for j in range(w):
            if i + j != 0 and values[i][j] == ".":
                LOG.debug((i, j, values[i][j]))
                dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i + 1][j]) % MODULO
    LOG.debug("\n".join(map(str, dp)))
    return dp[h][w]


def do_job():
    "Do the work"
    LOG.debug("Start working")
    # first line is number of test cases
    H, W = map(int, input().split())
    values = []
    for _ in range(H):
        values.append(input())
    result = solve(values, H, W)
    print(result)


def configure_log():
    "Configure the log output"
    log_formatter = logging.Formatter("L%(lineno)d - " "%(message)s")
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(log_formatter)
    LOG.addHandler(handler)


LOG = None
# for interactive call: do not add multiple times the handler
if not LOG:
    LOG = logging.getLogger("template")
    configure_log()


def main(argv=None):
    "Program wrapper."
    if argv is None:
        argv = sys.argv[1:]
    parser = ArgumentParser()
    parser.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        action="store_true",
        default=False,
        help="run as verbose mode",
    )
    args = parser.parse_args(argv)
    if args.verbose:
        LOG.setLevel(logging.DEBUG)
    do_job()
    return 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    sys.exit(main())


class memoized:
    """Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned, and
    not re-evaluated.
    """

    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
            value = self.func(*args)
            self.cache[args] = value
            return value
        except TypeError:
            # uncachable -- for instance, passing a list as an argument.
            # Better to not cache than to blow up entirely.
            return self.func(*args)

    def __repr__(self):
        """Return the function's docstring."""
        return self.func.__doc__

    def __get__(self, obj, objtype):
        """Support instance methods."""
        return functools.partial(self.__call__, obj)
