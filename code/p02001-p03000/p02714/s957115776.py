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
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

show_flg = False
# show_flg = True


def c(i, j, k):
    return j - i != k - j


def main():
    N = I()
    s = S()
    # N = 2000
    # s = 'R' * 2000
    R = [0] * (N+1)
    G = [0] * (N+1)
    B = [0] * (N+1)

    for i in range(N):
        if s[i] == 'R':
            R[i] += 1
        elif s[i] == 'G':
            G[i] += 1
        elif s[i] == 'B':
            B[i] += 1
        R[i+1] = R[i]
        G[i+1] = G[i]
        B[i+1] = B[i]

    ans = 0
    for i in range(N):
        for j in range(i, N):
            if s[i] == 'R' and s[j] == 'G' or s[i] == 'G' and s[j] == 'R':
                nxt = j - i + j
                if nxt >= len(s):
                    ans += B[N] - B[j]
                elif s[nxt] != 'B':
                    ans += B[N] - B[j]
                else:
                    ans += B[N] - B[j]
                    ans -= 1
            elif s[i] == 'R' and s[j] == 'B' or s[i] == 'B' and s[j] == 'R':
                nxt = j - i + j
                if nxt >= len(s):
                    ans += G[N] - G[j]
                elif s[nxt] != 'G':
                    ans += G[N] - G[j]
                else:
                    ans += G[N] - G[j]
                    ans -= 1
            elif s[i] == 'B' and s[j] == 'G' or s[i] == 'G' and s[j] == 'B':
                nxt = j - i + j
                if nxt >= len(s):
                    ans += R[N] - R[j]
                elif s[nxt] != 'R':
                    ans += R[N] - R[j]
                else:
                    ans += R[N] - R[j]
                    ans -= 1


    print(ans)
    # print(R)
    # print(G)
    # print(B)


if __name__ == '__main__':
    main()
