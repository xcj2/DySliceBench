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


def debug(table, *args):
    ret = []
    for name, val in table.items():
        if val in args:
            ret.append('{}: {}'.format(name, val))
    print(' | '.join(ret), file=sys.stderr)


yn = {False: 'No', True: 'Yes'}
YN = {False: 'NO', True: 'YES'}
MOD = 10**9+7
inf = float('inf')
IINF = 10**19
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

show_flg = False
# show_flg = True


def c(i, j, k):
    return j - i != k - j


def main():
    N = I()
    s = S()
    r, g, b = 0, 0, 0

    for i in range(N):
        if s[i] == 'R':
            r += 1
        elif s[i] == 'G':
            g += 1
        else:
            b += 1

    all_c = r * g * b
    sub = 0
    test = 0

    for i in range(N):
        for j in range(i+1, N):
            k = (j - i) + j
            if k >= N or s[i] == s[j] or s[k] == s[i] or s[j] == s[k]:
                continue
            # 全部異なる、等差である
            sub += 1

    # 全部異なる、等差でないを求める
    print(all_c - sub)


if __name__ == '__main__':
    main()
