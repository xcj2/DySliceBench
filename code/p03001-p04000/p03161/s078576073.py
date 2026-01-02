#!/usr/bin/env python3
# vim: set fileencoding=utf-8

# pylint: disable=unused-import, invalid-name, missing-docstring, bad-continuation


"""Module docstring
"""

import sys


def solve(values, nb, max_jump_size):
    max_jump_size = min(nb, max_jump_size)
    cost_to = [0]
    for i in range(1, nb):
        j = max(0, i - max_jump_size)
        value_i = values[i]
        new_cost = min(
            prev_cost + abs(value_i - prev_value)
            for prev_cost, prev_value in zip(cost_to[j:i], values[j:i])
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
