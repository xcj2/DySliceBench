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


YN = {False: 'NO', True: 'YES'}
yn = {False: 'No', True: 'Yes'}
MOD = 10**9+7
inf = float('inf')
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
# sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


show_flg = True
show_flg = False


def main():
    s = S()
    skip = [0] * len(s)

    for i in range(len(s)):
        if s[i:i+5] == 'dream':
            for idx in range(i, i+5):
                skip[idx] = 1

    for i in range(len(s)):
        if s[i:i+5] == 'erase':
            for idx in range(i, i+5):
                skip[idx] = 2

    for i in range(len(s)-1):
        if skip[i] == 0 and skip[i+1] == 0 and skip[i-1] == 1 and s[i] == 'e' and s[i+1] == 'r':
            skip[i] = 3
            skip[i+1] = 3

    for i in range(len(s)):
        if skip[i] == 0 and skip[i-1] == 2 and s[i] == 'r':
            skip[i] = 4

    print(YN[all(skip)])


if __name__ == '__main__':
    main()
