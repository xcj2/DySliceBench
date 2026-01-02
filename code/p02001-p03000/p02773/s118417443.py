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
    # nums = getlist()
    d = defaultdict(int)
    for i in range(n):
        s = input().strip()
        d[s] += 1
    # print(d)
    mx = max(d.values())
    ans = [k for (k, v) in d.items() if v == mx]

    ans.sort()
    for an in ans:
        print(str(an)[2:-1])

if __name__ == '__main__':
    main()

"""
9999
3

2916
"""