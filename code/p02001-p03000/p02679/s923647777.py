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

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def main():
    N = I()
    zero = 0
    cnts = defaultdict(int)
    used = set()

    for i in range(N):
        a, b = MI()
        if a == 0 and b == 0:
            zero += 1
            continue

        g = gcd(abs(a), abs(b))
        a = a // g
        b = b // g
        if b < 0:
            a = -a
            b = -b
        cnts[(a, b)] += 1

    # print(cnts)

    ans = 1
    for key, c in cnts.items():
        if key in used:
            continue
        a, b = key
        if a > 0:
            rev = (-b, a)
        else:
            rev = (b, -a)

        if rev in cnts:
            ans *= pow(2, cnts[key], MOD) + pow(2, cnts[rev], MOD) - 1
            # print(key, rev, ans)
            ans %= MOD
            used.add(rev)
        else:
            ans *= pow(2, cnts[key], MOD)

    ans += zero
    ans -= 1
    print(ans % MOD)
    # ans = 0
    # for i in range(2 ** N):
    #     groups = []
    #     for j in range(N):
    #         if ((i >> j) & 1):
    #             groups.append(j)

    #     if len(groups) == 0:
    #         continue

    #     c = 1
    #     for i in groups:
    #         for j in groups:
    #             if i == j:
    #                 continue
    #             if A[i] / float(B[i]) == (- B[j] / float(A[j])):
    #                 c = 0
    #                 break
    #     if c == 0:
    #         print(groups)
    #     ans += c
    # print(ans)

    # print(test1)
    # print(test2)
    # all = pow(2, N, MOD) - 1
    # red = 0
    # for i in range(N-1):
    #     left = A[i] / float(B[i])
    #     right = (- B[i] / float(A[i]))
    #     c = mr[left]
    #     if (N - i - 1 - c) >= 0 and c - 1 >= 0:
    #         red += pow(2, (N - i - 1 - c), MOD) * pow(2, c - 1, MOD)
    #         # print((N - i - 1 - c), c - 1)
    #         # print('red', red, 'left', left)
    #         red %= MOD
    #     # print(mr, mr[left])
    #     if ml[left] > 0:
    #         ml[left] -= 1
    #     if mr[right] > 0:
    #         mr[right] -= 1

    # # print(red)
    # print(all - red)


if __name__ == '__main__':
    main()
