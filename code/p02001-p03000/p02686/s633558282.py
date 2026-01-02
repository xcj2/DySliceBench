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
    zeros = []
    incs = []
    decs = []
    s = [None] * N

    for i in range(N):
        s[i] = S()
        cur = 0
        mn = 0
        for c in s[i]:
            if c == '(':
                cur += 1
            else:
                cur -= 1
            mn = min(mn, cur)
        end = cur

        if end == 0:
            zeros.append((mn, end, i))
        elif end > 0:
            incs.append((mn, end, i))
            # heappush(incs, (-mn, end))
        else:
            decs.append((mn - end, end, i))
            # heappush(decs, (mn, end))

    incs.sort(reverse=True)
    decs.sort()

    ans = []
    for mn, end, idx in incs:
        ans.append(s[idx])

    for mn, end, idx in zeros:
        ans.append(s[idx])

    for mn, end, idx in decs:
        ans.append(s[idx])

    now = 0
    for i in range(len(ans)):
        for c in ans[i]:
            if c == '(':
                now += 1
            else:
                now -= 1
            if now < 0:
                print("No")
                return

    print(yn[now == 0])

    # now = 0
    # for mn, end, idx in incs:
    #     if now + mn < 0:
    #         print('No')
    #         return
    #     now += end

    # for mn, end, idx in zeros:
    #     if now + mn < 0:
    #         print('No')
    #         return
    #     now += end

    # for mn, end, idx in decs:
    #     if now + mn < 0:
    #         print('No')
    #         return
    #     now += end

    # print(yn[now == 0])


if __name__ == '__main__':
    main()
