from collections import Counter
from itertools import groupby


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def ilen(ll):
    return sum(1 for _ in ll)


def solve():
    """
    2     3
    1(-1) 1
    """
    N = read_int()
    A = read_ints()
    counter = [0]*max(A)
    for a in A:
        counter[a-1] += 1
    remove = 0
    twos = 0
    for a in counter:
        if a > 0:
            if a%2 == 0:
                remove += (a-2)
                twos += 1
            else:
                remove += (a-1)
    if twos%2 == 0:
        remove += twos
    else:
        remove += twos+1
    return N-remove


if __name__ == '__main__':
    print(solve())
