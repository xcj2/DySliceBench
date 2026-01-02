#!/usr/bin/env python3
# vim: set fileencoding=utf-8

# pylint: disable=unused-import, invalid-name, missing-docstring, bad-continuation


"""Module docstring
"""

import sys
from collections import deque


def solve(values, nb, max_jump_size):
    max_jump_size = min(nb, max_jump_size)
    cost_to = [0]
    for i in range(1, nb):
        new_cost = min(
            cost_to[i - k] + abs(values[i] - values[i - k])
            for k in range(1, max_jump_size + 1)
            if i - k >= 0
        )
        cost_to.append(new_cost)
    return new_cost


def do_job():
    "Do the work"
    # first line is number of test cases
    N, K = map(int, input().split())
    values = list(map(int, input().split()))
    result = solve(values, N, K)
    print(result)


def print_output(testcase, result) -> None:
    "Formats and print result"
    if result is None:
        result = "IMPOSSIBLE"
    print("Case #{}: {}".format(testcase + 1, result))


def main(argv=None):
    "Program wrapper."
    if argv is None:
        argv = sys.argv[1:]
    do_job()
    return 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    sys.exit(main())
