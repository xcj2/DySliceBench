from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations, accumulate, product, combinations_with_replacement
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
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def print_matrix(mat):
    for i in range(len(mat)):
        print(*['IINF' if v == IINF else "{:0=4}".format(v) for v in mat[i]])


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
    X, K = MI()
    p = LI()
    diff = []
    ps = set(p)
    c = []

    for i in range(-100, 200):
        if i not in ps:
            c.append(i)

    for i in range(len(c)):
        n = (abs(c[i] - X), i)
        diff.append(n)

    diff.sort()

    # print(diff[:10])

    if len(diff) == 0:
        print(X)
    elif len(diff) == 1:
        print(c[diff[0][1]])
    elif len(diff) > 1:
        if diff[0][0] == diff[1][0]:
            a = c[diff[0][1]]
            b = c[diff[1][1]]
            print(min(a, b))
        else:
            a = c[diff[0][1]]
            print(a)


if __name__ == '__main__':
    main()
