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

def solve():
    a, v = getList()
    b, w = getList()
    t = getN()
    if w >= v:
        print("NO")
    else:
        if abs(a - b) <= t * (v - w):
            print("YES")
        else:
            print("NO")

def main():
    # n = getN()
    # for _ in range(n):
    solve()
if __name__ == "__main__":
    solve()
