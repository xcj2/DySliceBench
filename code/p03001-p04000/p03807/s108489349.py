import sys
# input = sys.stdin.buffer.readline
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getlist():
    return list(map(int, input().split()))
import math
import bisect
import heapq
from collections import defaultdict, Counter, deque
MOD = 10**9 + 7
INF = 10**15

def main():
    n = getN()
    nums = getlist()
    eo = [0, 0]
    for num in nums:
        eo[num % 2] += 1
    e = (eo[0] + eo[1] // 2) % 2
    o = eo[1] % 2
    if o == 0:
        print("YES")
    else:
        print("NO")
    # print(e,o)

if __name__ == '__main__':
    main()

"""
9999
3

2916
"""