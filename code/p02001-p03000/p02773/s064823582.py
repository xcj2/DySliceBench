from math import factorial
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


def MI(): return map(int, input().split())


def S(): return input()


def MS(): return map(str, input().split())


def LI(): return [int(i) for i in input().split()]


def LI_(): return [int(i)-1 for i in input().split()]


def StoI(): return [ord(i)-97 for i in input()]


def ItoS(nn): return chr(nn+97)


def input(): return sys.stdin.readline().rstrip()


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


def MS(): return map(str, input().split())


YN = {False: 'No', True: 'Yes'}
MOD = 10**9+7
inf = float('inf')
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


# show_flg = False
show_flg = True


def main():
    N = I()
    s = [None] * N
    m = {}

    for i in range(N):
        s[i] = S()
        m[s[i]] = 0

    for i in range(N):
        m[s[i]] += 1

    arr = []
    for (key, v) in m.items():
        arr.append((v, key))

    arr.sort(reverse=True)

    m = arr[0][0]
    ans = []
    for i in range(len(arr)):
        if m == arr[i][0]:
            ans.append(arr[i][1])

    ans.sort()
    for a in ans:
        print(a)


if __name__ == '__main__':
    main()
