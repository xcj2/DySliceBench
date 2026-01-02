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
MOD = 998244353
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

def main():
    n, m = getList()
    ans = 0
    for yaku in getyaku(m):
        if m // yaku >= n:
            if ans < yaku:
                ans = yaku
    print(ans)

if __name__ == "__main__":
    main()

