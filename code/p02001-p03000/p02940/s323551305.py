#!/usr/bin/env python3
import sys
from bisect import bisect_left
INF = float("inf")

MOD = 998244353  # type: int


def solve(N: int, S: str):

    count = 1
    nums = {"B": 0, "R": 0, "G": 0}
    other = {"B": "RG", "R": "BG", "G": "BR"}
    for c in S:
        buf = sorted(nums.values())
        if nums[c] == buf[2]:
            count *= N-nums[c]
            count %= MOD
        elif buf[1] == nums[c]:
            count *= buf[2]-buf[1]
            count %= MOD
        else:
            count *= buf[1]-buf[0]
            count %= MOD
            pre = "C"
        nums[c] += 1
    print(count)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)


if __name__ == '__main__':
    main()
