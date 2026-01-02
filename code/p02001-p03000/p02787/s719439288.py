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
    h, k = getlist()
    mag = []
    for i in range(k):
        mag.append((getlist()))
    dp = [INF for i in range(h+1)]
    dp[0] = 0
    for i in range(h):
        cur = dp[i]
        for ma in mag:
            a, b = ma
            if i + a >= h:
                tgt = h
            else:
                tgt = i + a
            if dp[tgt] > cur + b:
                dp[tgt] = cur + b
    print(dp[-1])
    # mag.sort()


if __name__ == '__main__':
    main()

"""
9999
3

2916
"""