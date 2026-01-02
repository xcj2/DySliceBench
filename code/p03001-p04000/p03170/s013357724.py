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


def solve_me(values, k):
    dp = [0 for _ in range(k)]
    # 1 is 1st player
    dp[k - 1] = 1
    for _ in range(k // min(values)):
        prev = dp.copy()
        # dp[i] which players can have i stones at round (1 first, 2 second, 3 both)
        dp = [0 for _ in range(k)]
        for a in values:
            LOG.debug((a))
            for i in range(a, k):
                # LOG.debug(("i", i, "prev[i]", prev[i]))
                # 1st player is there
                if prev[i] & 1 == 1:
                    # LOG.debug(("player 1", i - a))
                    dp[i - a] |= 2
                # 2nd player is there
                if prev[i] & 2 == 2:
                    # LOG.debug(("player 2", i - a))
                    dp[i - a] |= 1
        LOG.debug((dp))
        if dp[0] > 0:
            return dp[0] & 2
    assert False, dp
    return None


def solve(values, k):
    # dp[i] True if the first player wins if there are i stones remaining
    dp = [False for _ in range(k + 1)]
    for stones in range(k + 1):
        for a in values:
            if stones < a:
                continue
            if not dp[stones - a]:
                dp[stones] = True
        LOG.debug((dp))
    return dp[k]


def do_job():
    "Do the work"
    LOG.debug("Start working")
    # first line is number of test cases
    N, K = list(map(int, input().split()))
    values = list(map(int, input().split()))
    assert len(values) == N
    result = solve(values, K)
    print("First" if result else "Second")


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
