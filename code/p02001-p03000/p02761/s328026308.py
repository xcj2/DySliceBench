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


YNL = {False: 'No', True: 'Yes'}
YNU = {False: 'NO', True: 'YES'}
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

def digsum(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


def main():
    N, M = MI()
    s = [0] * M
    c = [0] * M
    d = [-1] * N
    d_list = [[] for i in range(N)]

    for i in range(M):
        s[i], c[i] = MI()
        d[s[i] - 1] = c[i]
        if len(d_list[s[i] - 1]) == 0 or d_list[s[i] - 1][-1] != c[i]:
            d_list[s[i] - 1].append(c[i])

    # print(*d)
    # print(d_list)
    for i in range(N):
        if len(d_list[i]) > 1:
            print(-1)
            return

    if len(d) > 1 and d[0] == 0:
        print(-1)
        return

    if len(d) == 1 and d[0] == -1:
        print(0)
        return

    for i in range(N):
        if d[i] == -1 and i == 0:
            d[i] = 1
        elif d[i] == -1:
            d[i] = 0

    print(''.join([str(i) for i in d]))


if __name__ == '__main__':
    main()
