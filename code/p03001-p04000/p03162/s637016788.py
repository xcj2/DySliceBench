#!/usr/bin/env python3
# vim: set fileencoding=utf-8

# pylint: disable=unused-import, invalid-name, missing-docstring, bad-continuation


"""Module docstring
"""

import sys


def solve(values, _nb):
    ca, cb, cc = 0, 0, 0
    for a, b, c in values:
        ca, cb, cc = max(cb + b, cc + c), max(ca + a, cc + c), max(ca + a, cb + b)
    return max(ca, cb, cc)


def do_job():
    "Do the work"
    # first line is number of test cases
    N = int(input().strip())
    values = []
    for _ in range(N):
        values.append(map(int, input().split()))
    result = solve(values, N)
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
