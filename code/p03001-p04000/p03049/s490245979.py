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


def print_matrix(mat):
    for i in range(len(mat)):
        print(*mat[i])


YNL = {False: 'No', True: 'Yes'}
YNU = {False: 'NO', True: 'YES'}
MOD = 10**9+7
inf = float('inf')
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
# sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


# show_flg = True
show_flg = False


def main():
    N = I()
    s = []

    for i in range(N):
        s.append(S())

    ans = 0
    a = 0
    b = 0
    dup = 0

    for i in range(N):
        if s[i][0] == 'B':
            b += 1
        if s[i][-1] == 'A':
            a += 1
        if s[i][0] == 'B' and s[i][-1] == 'A':
            dup += 1
        for j in range(1, len(s[i])):
            if s[i][j-1] == 'A' and s[i][j] == 'B':
                # print(j, s[i])
                ans += 1

    # print(dup, a, b, ans)
    if dup > 0 and dup == max(a, b):
        # print(dup, a, b)
        print(ans + dup - 1)
    else:
        print(ans + min(a, b))


if __name__ == '__main__':
    main()
