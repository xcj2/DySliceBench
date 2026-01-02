import sys
# input = sys.stdin.buffer.readline
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getlist():
    return list(map(int, input().split()))
def getlist2():
    return [int(x) * 100000 for x in input().split()]
import math
import bisect
import heapq
from decimal import Decimal
# from collections import defaultdict, Counter, deque
MOD = 10**9 + 7
INF = 10**15
def main():
    n,m = getlist()
    nums = getlist()
    sou = sum(nums)
    ans = 0
    for num in nums:
        if num >= sou / (4*m):
            ans += 1
    if ans >= m:
        print("Yes")
    else:
        print("No")
    return

if __name__ == '__main__':
    main()

"""
9999
3

2916
"""