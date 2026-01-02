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
import heapq
import sys
# sys.setrecursionlimit(1000000)
INF = 10 ** 17
MOD = 10 ** 9 + 7
def mint(lis):
    return list(map(int, lis))

def bifind(arr_sorted, x):
    idx = bisect_left(arr_sorted, x)
    if idx == len(arr_sorted):
        return False
    if arr_sorted[idx] == x:
        return True
    else:
        return False
def getyaku(n):
    ret = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            ret.append(i)
            ret.append(n // i)

    return ret

def find(x, a):
    idx = bisect_left(a, x)
    if idx == len(a):
        return False
    if a[idx] == x:
        return True
    else:
        return False

def main():
    # n = getN()
    h1, m1, h2, m2, k = getList()
    diff = h1*60 + m1 - h2*60 - m2
    print(-diff - k)
if __name__ == "__main__":
    main()

