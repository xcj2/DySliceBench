#!/usr/bin/env python3
# vim: set fileencoding=utf-8

# pylint: disable=unused-import, invalid-name, missing-docstring, bad-continuation


"""Module docstring
"""

import sys
from collections import defaultdict


def solve(values, _nb, max_capacity):
    dp = {}
    dp[0] = 0
    for w, v in values:
        keys = sorted(dp.keys(), reverse=True)
        for vk in keys:
            if vk + v in dp:
                dp[vk + v] = min(dp[vk + v], dp[vk] + w)
            else:
                dp[vk + v] = dp[vk] + w
    result = 0
    for v, w in dp.items():
        if w <= max_capacity and v > result:
            result = v
    return result


def solve_better(values, _nb, max_capacity):
    dp = [0] * (max_capacity + 1)
    for w, v in values:
        # dp = dp[:w] + [max(dp[j], dp[j - w] + v) for j in range(w, max_capacity + 1)]
        dp[w:] = [max(dpj, dpjw + v) for dpj, dpjw in zip(dp[w:], dp[:-w])]
    return dp[max_capacity]


def solve_slow(values, nb, max_capacity):
    dp = [[0 for _ in range(max_capacity + 1)] for _ in range(nb + 1)]
    for i in range(1, nb + 1):
        w, v = values[i - 1]
        for j in range(1, max_capacity + 1):
            if w <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
            else:
                dp[i][j] = dp[i - 1][j]
    # print("\n".join(map(str, dp)))
    return dp[nb][max_capacity]


INF = pow(10, 9) * 100


def solve_errichto(values, _nb, max_capacity):
    sum_values = sum(v for _w, v in values)
    # dp[i] min total weight of items with total value exactly i
    dp = [INF] * (sum_values + 1)
    dp[0] = 0
    for w, v in values:
        for value_already in range(sum_values - v, -1, -1):
            tmp = dp[value_already] + w
            if dp[value_already + v] > tmp:
                dp[value_already + v] = tmp
    result = 0
    for v, w in enumerate(dp):
        if w <= max_capacity:
            result = max(result, v)
    return result


def do_job():
    "Do the work"
    # first line is number of test cases
    N, W = map(int, input().split())
    values = []
    for _ in range(N):
        values.append(list(map(int, input().split())))
    result = solve_errichto(values, N, W)
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
