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


def LI(): return [int(i) for i in input().split()]


def LI_(): return [int(i)-1 for i in input().split()]


def StoI(): return [ord(i)-97 for i in input()]


def ItoS(nn): return chr(nn+97)


def input(): return sys.stdin.readline().rstrip()


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


def MS(): return map(str, input().split())

YN = ['No', 'Yes']
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

p = None
XY = None
N = None


def main():
    N, M = MI()
    ans = 0
    p = [0] * M
    S = [0] * M
    dic = {}
    # x = LI()

    for i in range(M):
        p[i], S[i] = MS()
        dic[p[i]] = {'AC': False, 'WA': 0}

    for i in range(M):
        if S[i] == 'WA' and dic[p[i]]['AC'] is False:
            dic[p[i]]['WA'] += 1
        elif S[i] == 'AC':
            dic[p[i]]['AC'] = True

    AC = 0
    WA = 0
    for key in dic.keys():
        if dic[key]['AC']:
            AC += 1
            WA += dic[key]['WA']

    print(AC, WA)


if __name__ == '__main__':
    main()
