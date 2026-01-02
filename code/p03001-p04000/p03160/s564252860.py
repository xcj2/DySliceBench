from bisect import bisect_left as bl
from bisect import bisect_right as br
from heapq import heappush,heappop
import math
from collections import *
from functools import reduce,cmp_to_key
import sys
input = sys.stdin.readline

M = mod = 10**9 +7
def factors(n):return sorted(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
def inv_mod(n):return pow(n, mod - 2, mod)

def li():return [int(i) for i in input().rstrip('\n').split()]
def st():return input().rstrip('\n')
def val():return int(input().rstrip('\n'))
def li2():return [i for i in input().rstrip('\n')]
def li3():return [int(i) for i in input().rstrip('\n')]
def li4():return [float(i) for i in input().rstrip('\n').split(' ')]








n = val()
l = li() + [2,2]

if n == 1:
    print(0)
    exit()
elif n == 2:
    print(abs(l[0] - l[1]))
    exit()
ans = [float('inf')]*(n + 2)
ans[0] = 0
for i in range(n):
    ans[i + 1] = min(ans[i + 1],ans[i] + abs(l[i] - l[i+1]))
    ans[i + 2] = min(ans[i + 2],ans[i] + abs(l[i] - l[i+2]))
print(ans[n-1])