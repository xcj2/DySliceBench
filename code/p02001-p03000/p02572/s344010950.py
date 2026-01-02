# -*- coding: utf-8 -*-
import sys
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect
import copy
sys.setrecursionlimit(10**6)

# lis_of_lis = [[] for _ in range(N)]


def zz():
    return list(map(int, sys.stdin.readline().split()))


def z():
    return int(sys.stdin.readline())


def S():
    return sys.stdin.readline()[:-1]


def C(line):
    return [sys.stdin.readline() for _ in range(line)]


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


MOD = pow(10, 9)+7

N = z()
A = zz()
ans = 0
part_sum = [0]*N
part_sum[0] = A[0]
sum_a = sum(A) % MOD
for i in range(1, N):
    part_sum[i] = (part_sum[i-1] + A[i]) % MOD

for i in range(N - 1):
    tmp = A[i]*(sum_a - part_sum[i])
    ans = (ans+tmp) % MOD
    ans = ans % MOD
print(ans)

# for i in range(N):
#     for j in range(i + 1, N):
#         ans += A[i]*A[j]
#         ans %= MOD
# print(ans)
