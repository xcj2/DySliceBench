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

show_flg = False
# show_flg = True


def main():
    H, W = MI()
    alpha = [0] * len(l_alp)

    for i in range(H):
        s = S()
        for j in range(W):
            alpha[ord(s[j])-97] += 1

    for i in range((H+1)//2):
        for j in range((W+1)//2):
            V = 4
            if H % 2 != 0 and i == (H+1)//2-1:
                V //= 2
            if W % 2 != 0 and j == (W+1)//2-1:
                V //= 2
            f = False

            if V == 2:
                for k in range(len(alpha)):
                    if alpha[k] % 2 == 0 and alpha[k] % 4 == 2:
                        f = True
                        alpha[k] -= V
                        break

            if not f:
                for k in range(len(alpha)):
                    if alpha[k] >= V:
                        f = True
                        alpha[k] -= V
                        break
            # print(i+1, j+1, V, alpha)
            if not f:
                print('No')
                return
    # print(alpha)
    print('Yes')

if __name__ == '__main__':
    main()
