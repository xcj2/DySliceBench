
from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations
import sys
import bisect
import string
import math
import time
#import random


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

YN = ['Yes', 'No']
MOD = 10**9+7
inf = float('inf')
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)


show_flg = False
# show_flg = True

def main():
    N = I()
    T, A = MI()
    H = LI()
    TMP = []

    for i in range(N):
        TMP.append(T - H[i] * 0.006)

    mn = 10**19
    ans = 0
    for i in range(N):
        if mn > abs(TMP[i] - A):
            mn = abs(TMP[i] - A)
            ans = i

    print(ans + 1)


if __name__ == '__main__':
    main()
