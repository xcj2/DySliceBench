# python3

#===============================================================================
from collections import defaultdict, Counter
from functools import lru_cache
from heapq import heappush, heappop
from math import gcd, floor, ceil
from sys import stdin, stdout

def ilist():
    return [int(x) for x in stdin.readline().strip().split(" ")]
def iint():
    return int(stdin.readline().strip())
def istr():
    return stdin.readline().strip()
##==============================================================================


def solve():
    pass


if __name__ == '__main__':
    N, K = ilist()
    di = [0] * (N + 1)
    for _ in range(K):
        d = iint()
        A = ilist()
        for i in range(d):
            di[A[i]] = 1
    print(N - sum(di))
