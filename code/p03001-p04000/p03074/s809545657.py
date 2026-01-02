from itertools import groupby
from collections import deque


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def ilen(v):
    return sum(1 for _ in v)


def solve():
    N, K = read_ints()
    S = input()
    counts = deque([])
    zeroes = 0
    total = 0
    max_total = 0
    for k, v in groupby(S):
        if k == '0':
            zeroes += 1
        this_count = ilen(v)
        total += this_count
        counts.append((k, this_count))
        while zeroes > K:
            k, count = counts.popleft()
            total -= count
            if k == '0':
                zeroes -= 1
        max_total = max(max_total, total)
    return max_total


if __name__ == '__main__':
    print(solve())
