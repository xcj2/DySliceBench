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
    s = S()
    N = len(s)

    for i in range(2):
        for j in range(2):
            for k in range(2):
                A = int(s[0])
                B = int(s[1])
                C = int(s[2])
                D = int(s[3])
                ans = A
                op1 = '+' if i == 0 else '-'
                op2 = '+' if j == 0 else '-'
                op3 = '+' if k == 0 else '-'
                ans = ans + B if i == 0 else ans - B
                ans = ans + C if j == 0 else ans - C
                ans = ans + D if k == 0 else ans - D
                if ans == 7:
                    print(s[0] + op1 + s[1] + op2 + s[2] + op3 + s[3] + '=7')
                    return

    print(-1)


if __name__ == '__main__':
    main()
