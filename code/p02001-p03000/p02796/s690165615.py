from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations, accumulate
import sys
import bisect
import string
import math
import time


def I(): return int(input())


def S(): return input()


def MI(): return map(int, input().split())


def MS(): return map(str, input().split())


def LI(): return [int(i) for i in input().split()]


def LI_(): return [int(i)-1 for i in input().split()]


def StoI(): return [ord(i)-97 for i in input()]


def ItoS(nn): return chr(nn+97)


def input(): return sys.stdin.readline().rstrip()


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


YN = ['No', 'Yes']
MOD = 10**9+7
inf = float('inf')
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

show_flg = False
# show_flg = True


def erase_overlap_intervals(intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        result, prev = 0, 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[prev][1]:
                if intervals[i][1] < intervals[prev][1]:
                    prev = i
                result += 1
            else:
                prev = i
        return result


def main():
    N = I()
    XL = [None] * N

    for i in range(N):
        X, L_ = MI()
        XL[i] = (X, L_, i)

    arr = [None] * N
    for i in range(N):
        arr[i] = (XL[i][0] - XL[i][1], XL[i][0] + XL[i][1])

    arr = sorted(arr, key=lambda a: a[1])
    print(N - erase_overlap_intervals(arr))


if __name__ == '__main__':
    main()
