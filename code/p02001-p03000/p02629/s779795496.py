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

ret = []

def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n) + ',' +str(X%n)
    return str(X%n)

def main():
    N = I()

    l = 0
    c = 1
    cur = N
    last = cur
    while True:
        cur -= 26 ** c
        c += 1
        if cur < 0:
            break
        last = cur

    if last == 0:
        l = c - 2
        # print('last=0', l, last)
        d = Base_10_to_n(last, 25).split(',')
        # print(d)

        print(l * 'z')
    else:
        l = c - 1
        ans = []

        last -= 1

        if last == 0:
            print(l * 'a')
            return

        while last > 0:
            # print('last', last)
            r = last % 26
            last //= 26
            # print('last', last)
            # print('r', l_alp[r])
            ans.append(l_alp[r])

        while len(ans) < l:
            ans.append('a')
        ans = ans[::-1]
        temp = ''
        for a in ans:
            temp += a
        print(temp)
    # print(d)

    # for i in range(1, 27):
    #     N = i
    #     while N > 0:
    #         r = N % 26
    #         N = N // 26

            # print('N', N, 'r', r, l_alp[r])

    # for N in range(1, 27):
    #     d = Base_10_to_n(N, 26).split(',')
    #     ans = ''

    #     print(N, d)

    #     for i in d:
    #         ans += l_alp[int(i)]

    #     print(ans)


if __name__ == '__main__':
    main()
