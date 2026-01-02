#!/usr/bin/env python3
# vim: set fileencoding=utf-8

# pylint: disable=unused-import, invalid-name, missing-docstring, bad-continuation


"""Module docstring
"""

import functools
import heapq
import logging
import math
import random
import string
import sys
from argparse import ArgumentParser
from collections import defaultdict
from copy import deepcopy


def solve(values, nb):
    cost_to = [0] * nb
    cost_to[1] = abs(values[1] - values[0])
    for i in range(2, nb):
        cost_to[i] = min(
            cost_to[i - 2] + abs(values[i] - values[i - 2]),
            cost_to[i - 1] + abs(values[i] - values[i - 1]),
        )
    return cost_to[nb - 1]


def do_job():
    "Do the work"
    LOG.debug("Start working")
    # first line is number of test cases
    N = int(input())
    values = list(map(int, input().split()))
    result = solve(values, N)
    print(result)


def print_output(testcase, result) -> None:
    "Formats and print result"
    if result is None:
        result = "IMPOSSIBLE"
    print("Case #{}: {}".format(testcase + 1, result))


def configure_log(log_file=None) -> None:
    "Configure the log output"
    log_formatter = logging.Formatter(
        "%(asctime)s - %(filename)s:%(lineno)d - " "%(levelname)s - %(message)s"
    )
    if log_file:
        handler = logging.FileHandler(filename=log_file)
    else:
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
