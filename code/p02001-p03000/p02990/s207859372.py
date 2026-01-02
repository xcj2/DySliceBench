import sys
import bisect
import collections
import fractions
import heapq
import math
from operator import mul
from functools import reduce


def permutation(n, r):
    if r == 0:
        return 1
    else:
        return reduce(mul, range(n, n - r, -1))


def combination(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    else:
        return reduce(mul, range(n, n - r, -1)) // reduce(mul, range(1, r + 1))


def fermat_s_little_theorem(denominator_no, molecule_no1, molecule_no2, mod):
    denominator = 1
    for i in range(1, denominator_no + 1):
        denominator = (denominator * i) % mod
    molecule = 1
    for i in range(1, molecule_no1 + 1):
        molecule = (molecule * i) % mod
    for i in range(1, molecule_no2 + 1):
        molecule = (molecule * i) % mod
    return denominator * pow(molecule, mod - 2, mod) % mod


def slove():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n, k = list(map(int, input().rstrip('\n').split()))
    for i in range(1, k + 1):
        if k - 1 >= i - 1 and n - k + 1 >= i:
            print(combination(n - k + 1, i) % mod * combination(k-1, i-1) % mod)
        else:
            print(0)


if __name__ == '__main__':
    slove()
