import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
from itertools import accumulate, permutations, combinations, product, groupby, combinations_with_replacement
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N, K = MAP()

A = LIST()

plus0 = []
minus = []
zero = []

for a in A:
    if a >= 0:
        plus0.append(a)
    if a == 0:
        zero.append(a)
    if a < 0:
        minus.append(a)

# print(plus0)
# print(minus)
# print(zero)

if (len(minus) == N and K%2 == 1) or (plus0 and minus and N == K and len(minus)%2 == 1):
    # 答えはマイナスなので最小化を目指す
    if (len(minus) == N and K%2 == 1):
        minus.sort(reverse=True)  # 小さい方からKこ
        ans = 1
        for i in range(K):
            ans *= minus[i]
            ans %= mod
    else:
        ans = 1
        for x in minus+plus0:
            ans *= x
            ans %= mod
    print(ans)
else:
    if len(plus0) == N:
        ans = 1
        plus0.sort(reverse=True)
        for i in range(K):
            ans *= plus0[i]
            ans %= mod
        print(ans)
        exit()

    # 答えは0以上なので最大化を目指す
    ans = 1
    cnt = 0
    plus0.sort()
    minus.sort(reverse=True)
    # print(plus0)
    # print(minus)
    while cnt != K:
        if cnt == K-1 or len(minus) <= 1:
            ans *= plus0.pop()
            cnt += 1
        else:
            if not plus0:
                ans *= minus.pop()
                ans *= minus.pop()
                cnt += 2
            elif len(plus0) == 1:
                if plus0[0] > minus[-1]*minus[-2]:
                    ans *= plus0.pop()
                    cnt += 1
                else:
                    ans *= minus.pop()
                    ans *= minus.pop()
                    cnt += 2
            else:
                if plus0[-1]*plus0[-2] > minus[-1]*minus[-2]:
                    ans *= plus0.pop()
                    cnt += 1
                else:
                    ans *= minus.pop()
                    ans *= minus.pop()
                    cnt += 2
        ans %= mod
    print(ans)
