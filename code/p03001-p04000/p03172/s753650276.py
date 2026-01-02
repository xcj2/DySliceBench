from decimal import *
from bisect import bisect_left as bl
from bisect import bisect_right as br
from heapq import heappush,heappop
import math
from collections import *
from functools import reduce,cmp_to_key
import sys
input = sys.stdin.readline

M = mod = 10**9 + 7
def factors(n):return sorted(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
def inv_mod(n):return pow(n, mod - 2, mod)

def li():return [int(i) for i in input().rstrip('\n').split()]
def st():return input().rstrip('\n')
def val():return int(input().rstrip('\n'))
def li2():return [i for i in input().rstrip('\n')]
def li3():return [int(i) for i in input().rstrip('\n')]
def li4():return [float(i) for i in input().rstrip('\n').split(' ')]



n,k = li()
l = sorted(li())
dp = [0]*(k + 1)
helparr = [0] + [1 for i in range(k + 1)]




for i in range(l[0] + 1):dp[i] = 1

curr = 0
for j in range(k + 1):
    curr += dp[j]
    helparr[j + 1] = curr




for i in l[1:]:
    for j in range(k,-1,-1):
        leftind = max(0,j - i)
        dp[j] = (dp[j] + helparr[j] - helparr[leftind])%mod


    curr = 0
    for j in range(k + 1):
        curr += dp[j]
        helparr[j + 1] = curr



print(dp[-1])

