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


def make4(initial, L, M, N, O):
    return [[[[initial for i in range(O)]
                for n in range(N)]
                for m in range(M)]
                for l in range(L)]


def make3(initial, L, M, N):
    return [[[initial for n in range(N)]
                for m in range(M)]
                for l in range(L)]


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


def main():
    N = I()
    A = LI()
    dp_use = [-IINF] * 3
    dp_not_use = [-IINF] * 3
    dp_not_use[0] = 0

    for i in range(N):
        dp_use_next = [-IINF] * 3
        dp_not_use_next = [-IINF] * 3

        for j in range(3):
            if j - 1 >= 0:
                dp_not_use_next[j] = max(dp_use[j], dp_not_use[j-1])
            else:
                dp_not_use_next[j] = dp_use[j]
            dp_use_next[j] = dp_not_use[j] + A[i]

        # print('dp_use    ', *[a if a > -10**10 else '-IINF' for a in dp_use_next])
        # print('dp_not_use', *[a if a > -10**10 else '-IINF' for a in dp_not_use_next])
        dp_use = dp_use_next
        dp_not_use = dp_not_use_next

    if N % 2 == 0:
        print(max(dp_use[1], dp_not_use[0]))
    else:
        print(max(dp_use[2], dp_not_use[1]))


if __name__ == '__main__':
    main()
