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
    dp_use = [-IINF] * 5
    dp_not_use = [-IINF] * 5
    dp_not_use[0] = 0

    for k in range(N):
        dp_use_next = [-IINF] * 5
        dp_not_use_next = [-IINF] * 5
        for current_dif in range(-3,2):
            if current_dif-1 >= -3:
                dp_use_next[current_dif] = dp_not_use[current_dif - 1] + A[k]
            if current_dif+1 < 2:
                dp_not_use_next[current_dif] = max(dp_use[current_dif+1], dp_not_use[current_dif+1])
        dp_use = dp_use_next
        dp_not_use = dp_not_use_next

    dif = N//2 - (N-N//2)
    print(max(dp_use[dif], dp_not_use[dif]))


if __name__ == '__main__':
    main()
