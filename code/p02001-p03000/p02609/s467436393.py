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
    N = I()
    X = S()
    bit_cnt = X.count('1')
    one_inv_cnt = bit_cnt - 1
    zero_inv_cnt = bit_cnt + 1
    MAX = 2 * 10 ** 5 + 1

    # 大きい数の余り
    # 繰り返し２乗法の発展？
    zero_mod = 0
    one_mod = 0
    for i in range(0, len(X)):
        b = int(X[i])
        if one_inv_cnt != 0:
            one_mod = (one_mod * 2 + b) % one_inv_cnt
        zero_mod = (zero_mod * 2 + b) % zero_inv_cnt

    f = [0] * MAX
    for i in range(1, MAX):
        f[i] = f[i % str(bin(i)).count('1')] + 1

    for i in range(len(X)-1, -1, -1):
        if X[N-1-i] == '1':
            if one_inv_cnt != 0:
                nxt = one_mod
                nxt -= pow(2, i, one_inv_cnt)
                nxt %= one_inv_cnt
                print(f[nxt] + 1)
            else:
                print(0)
        else:
            nxt = zero_mod
            nxt += pow(2, i, zero_inv_cnt)
            nxt %= zero_inv_cnt
            print(f[nxt] + 1)


if __name__ == '__main__':
    main()
