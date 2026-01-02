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
    bingo = []
    punched = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        bingo.append(getlist())

    n = getN()
    for ball in range(n):
        num = getN()
        for i, row in enumerate(bingo):
            for j, cell in enumerate(row):
                if num == cell:
                    punched[i][j] = 1

    for row in punched:
        if sum(row) == 3:
            print("Yes")
            return

    for i in range(3):
        if punched[0][i] and punched[1][i] and punched[2][i]:
            print("Yes")
            return

    if punched[0][0] and punched[1][1] and punched[2][2]:
        print("Yes")
        return

    if punched[0][2] and punched[1][1] and punched[2][0]:
        print("Yes")
        return

    print("No")
    return

if __name__ == '__main__':
    main()

"""
9999
3

2916
"""