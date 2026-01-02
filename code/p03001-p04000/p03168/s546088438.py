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


def prob(i, values):
    result = 1
    idx = 0
    for idx, v in enumerate(values):
        i, rest = divmod(i, 2)
        if rest == 1:
            result *= v
        else:
            result *= 1 - v
        idx += 1
    return result


def solve(values, nb):
    LOG.debug((values))
    dp = [[0] * (nb + 1) for _ in range(nb // 2 + 1)]
    dp[0][0] = 1
    for j in range(1, nb + 1):
        dp[0][j] = dp[0][j - 1] * (1 - values[j - 1])
    total = dp[0][-1]
    for i in range(1, nb // 2 + 1):
        for j in range(i, nb + 1):
            dp[i][j] = (
                dp[i - 1][j - 1] * values[j - 1] + (1 - values[j - 1]) * dp[i][j - 1]
            )
        total += dp[i][-1]
    # LOG.debug(("\n" + "\n".join(map(str, dp))))
    return 1 - total


def do_job():
    "Do the work"
    LOG.debug("Start working")
    # first line is number of test cases
    N = int(input())
    values = list(map(float, input().split()))
    # values = []
    # for _ in range(N):
    #     values.append(input().split())
    result = solve(values, N)
    # 6 digits float precision {:.6f} (6 is the default value)
    print("{:.10g}".format(result))


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
