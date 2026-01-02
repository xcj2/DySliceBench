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

n,m = li()
l = []

for i in range(n):l.append(li2())
l[0][0] = 1


for i in range(1,n):l[i][0] = 1*l[i-1][0] if l[i][0] != '#' else 0

for j in range(1,m):l[0][j] = 1*l[0][j-1] if l[0][j] != '#' else 0

for i in range(1,n):
    for j in range(1,m):
        if l[i][j] != '#':
            l[i][j] = l[i-1][j] + l[i][j-1]
        else:l[i][j] = 0
        l[i][j]%=mod

print(l[-1][-1])