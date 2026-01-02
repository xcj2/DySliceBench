def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))

from collections import defaultdict, deque
from sys import exit
import math
import copy
from bisect import bisect_left, bisect_right
from heapq import *
import sys
# sys.setrecursionlimit(1000000)
INF = 10 ** 17
MOD = 1000000007

from fractions import *
def inverse(f):
    # return Fraction(f.denominator,f.numerator)
    return 1/f

def make_next(n, nums):
    imos = [0 for i in range(n)]
    for i, num in enumerate(nums):
        if num > i:
            imos[0] += 1
        else:
            imos[i - num] += 1

        if i + num + 1 < n:
            imos[i+num+1] -= 1
    # print(imos)
    nx = []
    tmp = 0
    for im in imos:
        tmp += im
        nx.append(tmp)

    return nx

def mantan_check(n, nums):
    if sum(nums) == n ** 2:
        return True
    else:
        return False

def solve():
    n, k = getList()
    nums = getList()
    for i in range(k):
        nums = make_next(n, nums)
        if mantan_check(n, nums):
            print(*nums)
            return

    print(*nums)
    return



def main():
    # n = getN()
    # for _ in range(n):
    solve()
if __name__ == "__main__":
    solve()

"""
5 10000000000000
4 0 0 0 0
"""