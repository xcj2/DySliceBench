import sys
# input = sys.stdin.buffer.readline
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getlist():
    return list(map(int, input().split()))
import math
import heapq
import bisect
from collections import defaultdict, Counter, deque
MOD = 10**9 + 7
INF = 10**21

def main():
    n, m = getlist()
    numbers = [-1 for i in range(n)]
    for query in range(m):
        a, b = getlist()
        if numbers[a-1] != b and numbers[a-1] != -1:
            print(-1)
            return
        else:
            numbers[a-1] = b
    if n == 1 and numbers[0] <= 0:
        print(0)
        return

    if numbers[0] == 0:
        print(-1)
        return

    elif numbers[0] == -1:
        numbers[0] = 1

    for i, num in enumerate(numbers):
        if num == -1:
            numbers[i] = 0

    print("".join(list(map(str, numbers))))


if __name__ == '__main__':
    main()

"""
9999
3

2916
"""