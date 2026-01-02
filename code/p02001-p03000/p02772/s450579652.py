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
    n = getN()
    # n, m = getlist()
    nums = getlist()
    for num in nums:
        if num % 2 == 0 and num % 3 != 0 and num % 5 != 0:
            print("DENIED")
            return

    print("APPROVED")

if __name__ == '__main__':
    main()

"""
9999
3

2916
"""