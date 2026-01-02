from bisect import bisect_left as bl
from bisect import bisect_right as br
from heapq import heappush,heappop
from math import floor,ceil
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
def li2():return [i for i in input().rstrip('\n').split(' ')]
def li3():return [int(i) for i in input().rstrip('\n')]


s = st()
q = val()
l = []

cou = 0

d = deque()
for i in s:d.append(i)


for j in range(q):
    l = li2()
    if len(l) == 1:cou = not cou
    else:
        if cou:
            a = 3 - int(l[1])
        else:a = int(l[1])
        if a == 2:
            d.append(l[-1])
        else:d.appendleft(l[-1])

s = ''.join(e for e in d)
if cou:s = s[::-1]
print(s)

