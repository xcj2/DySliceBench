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
#===============================================================================


def solve(A):
    N = len(A)
    res = 0
    X = [A[i] + i for i in range(N)]
    Y = [A[i] - i for i in range(N)]
    #print(X, Y)
    d1 = Counter(X)
    d2 = Counter(Y)
    #print(d1, d2)
    for k in d1:
        res += d1[k] * d2[-k]
    return res


if __name__ == '__main__':
    N = iint()
    A = ilist()
    print(solve(A))
