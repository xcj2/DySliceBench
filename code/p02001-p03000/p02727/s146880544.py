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


def print_matrix(mat):
    for i in range(len(mat)):
        print(*mat[i])


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


def main():
    X, Y, A, B, C = MI()
    p = LI()
    q = LI()
    r = LI()
    ans = 0
    p = sorted(p, reverse=True)
    q = sorted(q, reverse=True)
    r = sorted(r, reverse=True)
    p = p[:X]
    q = q[:Y]
    hp = []
    hq = []
    hr = []

    for i in p:
        heappush(hp, i)

    for i in q:
        heappush(hq, i)

    for i in r:
        heappush(hr, -i)

    while len(hr) != 0:
        vr = -heappop(hr)
        vp = heappop(hp)
        vq = heappop(hq)

        if vp < vq and vr > vp:
            heappush(hp, vr)
            heappush(hq, vq)
        elif vp >= vq and vr > vq:
            heappush(hp, vp)
            heappush(hq, vr)
        else:
            heappush(hp, vp)
            heappush(hq, vq)

    print(sum(hp) + sum(hq))

if __name__ == '__main__':
    main()
