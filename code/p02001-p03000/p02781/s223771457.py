#!/usr/bin/env python
from collections import deque

def comb(a, b):
    result = 1
    for i in range(b):
        result *= (a - i) / (i + 1)
    return result

def zero_num(n, k):
    if k == 0:
        return 1
    if len(n) == 0:
        return 0
    if n[0] == 0:
        return zero_num(n[1:], k)

    rest = comb(len(n) - 1, k) * 9 ** k
    rest += (n[0]-1) * comb(len(n) - 1, k-1) * 9 ** (k-1)
    return int(rest + zero_num(n[1:], k-1))


def main():
    N = tuple(map(int, input()))
    K = int(input())

    print(zero_num(N, K))


if __name__ == '__main__':
    main()
