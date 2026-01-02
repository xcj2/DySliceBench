from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations, accumulate, product
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


def debug(table, *args):
    ret = []
    for name, val in table.items():
        if val in args:
            ret.append('{}: {}'.format(name, val))
    print(' | '.join(ret), file=sys.stderr)


yn = {False: 'No', True: 'Yes'}
YN = {False: 'NO', True: 'YES'}
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

def rec(li, i, M, N, a, b, c, d, cans):
    # print(i, li, len(li), N)
    if len(li) >= N:
        # print(li, N)
        ans = 0
        for j in range(len(a)):
            if li[b[j]-1] - li[a[j]-1] == c[j]:
                ans += d[j]
        # print(ans, li)
        return ans

    # for j in range(1, len(lis[i])):
    #     for v in lis[i][j]:

    ans = 0
    if len(cans[i]) == 0:
        ans = max(ans, rec(li + [1], i+1, M, N, a, b, c, d, cans))
    else:
        for v in cans[i]:
            ans = max(ans, rec(li + [v], i+1, M, N, a, b, c, d, cans))

    return ans


def main():
    N, M, Q = MI()
    a = [0] * Q
    b = [0] * Q
    c = [0] * Q
    d = [0] * Q
    didx = [None] * Q
    lis = [[[] for i in range(N+1)] for i in range(N+1)]
    cans = [set() for i in range(N+1)]

    for i in range(Q):
        a[i], b[i], c[i], d[i] = MI()
        # didx[i] = (d[i], i)

    ans = 0
    A = [i for i in range(1, M + 1)]
    for v in itertools.combinations_with_replacement(A, N):
        tmp = 0
        for j in range(len(a)):
            if v[b[j]-1] - v[a[j]-1] == c[j]:
                tmp += d[j]
        ans = max(ans, tmp)

    print(ans)


if __name__ == '__main__':
    main()
