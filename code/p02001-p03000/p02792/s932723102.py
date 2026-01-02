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


YN = ['No', 'Yes']
MOD = 10**9+7
inf = float('inf')
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


show_flg = True
show_flg = False


def cmb(n, r):
    if n - r < r:
        r = n - r
    if r == 0:
        return 1
    if r == 1:
        return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2, r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1, r, p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result


def main():
    N = I()
    NS = str(N)
    ans = 0

    dic = {}

    for j in range(1, 10):
        for k in range(1, 10):
            if j != k:
                dic[10 * j + k] = 0
            else:
                dic[j] = 0

    for i in range(1, N+1):
        if i < 10:
            dic[i] += 1
        else:
            b = int(str(i)[0])
            e = int(str(i)[-1])
            if b == e:
                dic[b] += 1
            elif e != 0:
                dic[10 * b + e] += 1

    # print(dic)
    for j in range(0, 10):
        for k in range(0, 10):
            if 10 * j + k in dic:
                if 10 * j + k < 10:
                    ans += dic[10 * j + k] * dic[10 * j + k]
                else:
                    ans += dic[10 * j + k] * dic[10 * k + j]
    print(ans)


if __name__ == '__main__':
    main()
