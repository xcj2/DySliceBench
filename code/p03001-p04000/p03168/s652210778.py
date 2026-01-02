from decimal import *
from bisect import bisect_left as bl
from bisect import bisect_right as br
from heapq import heappush,heappop
import math
from collections import *
from functools import reduce,cmp_to_key
import sys
input = sys.stdin.readline

M = mod = 998244353
def factors(n):return sorted(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
def inv_mod(n):return pow(n, mod - 2, mod)

def li():return [int(i) for i in input().rstrip('\n').split()]
def st():return input().rstrip('\n')
def val():return int(input().rstrip('\n'))
def li2():return [i for i in input().rstrip('\n')]
def li3():return [int(i) for i in input().rstrip('\n')]
def li4():return [float(i) for i in input().rstrip('\n').split(' ')]

n = val()
l = li4()
mihe = n//2 + 1


curr = 1
for i in l:curr *= (1 - i)
dp = [0 for i in range(n + 1)]
dp[0] = 1

for i in range(n):

    for j in range(i + 1,-1,-1):
        if not j:dp[j] *= 1 - l[i]
        else:dp[j] = dp[j-1] * l[i] + dp[j] *(1 - l[i])

ans = 0
for i in dp[-mihe:]:
    ans += i

print(round(ans,10))