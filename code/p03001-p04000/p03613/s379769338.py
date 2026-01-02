import math
from itertools import groupby


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def ilen(it):
    return sum(1 for _ in it)


def solve():
    N = read_int()
    A = read_ints()
    A.sort()
    grouped = [(a, ilen(v)) for a, v in groupby(A)]
    max_count = -math.inf
    for i in range(len(grouped)):
        count = grouped[i][1]
        if i > 0 and grouped[i][0]-1 == grouped[i-1][0]:
            count += grouped[i-1][1]
        if i < len(grouped)-1 and grouped[i][0]+1 == grouped[i+1][0]:
            count += grouped[i+1][1]
        max_count = max(max_count, count)
    return max_count


if __name__ == '__main__':
    print(solve())
