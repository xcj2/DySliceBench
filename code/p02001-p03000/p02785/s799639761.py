import sys
input = sys.stdin.buffer.readline
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getlist():
    return list(map(int, input().split()))
import math
import heapq
from collections import defaultdict, Counter, deque
MOD = 10**9 + 7
INF = 10**15


def main():
    n, k = getlist()
    nums = getlist()
    nums.sort()
    if n <= k:
        print(0)
        return
    if k == 0:
        print(sum(nums))
        return
    print(sum(nums[:-k]))

if __name__ == '__main__':
    main()

"""
9999
3

2916
"""