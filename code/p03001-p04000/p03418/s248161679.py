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


yn = ['Yes', 'No']
YN = ['YES', 'NO']
MOD = 10**9+7
inf = float('inf')
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)


show_flg = False
# show_flg = True


def main():
    N, K = MI()
    # arr = [[0] * N for i in range(N)]

    if K == 0:
        print(N * N)
        return

    # for b in range(1, N+1):
    #     for a in range(1, N+1):
    #         arr[b-1][a-1] = a % b

    ans = 0
    for b in range(N):
        if K <= (b + 1) - 1:
            # print(b+1, arr[b])
            loop = N // (b+1)
            r = N % (b+1)
            ans += loop * ((b+1) - K)
            ans += max(0, r - K + 1)
            # print(ans, loop * ((b+1) - K), r - K + 1)
    print(ans)


if __name__ == '__main__':
    main()
