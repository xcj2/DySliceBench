import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

N = I()
A = LI()

def primes(n):
    if n <= 1:
        return []
    is_prime = [True]*(n+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2,int(n**0.5)+1):
        if is_prime[i]:
            for j in range(2*i,n+1,i):
                is_prime[j] = False
    return [i for i in range(2,n+1) if is_prime[i]]

from functools import reduce
def calc_gcd(A):
    return reduce(math.gcd, A)

def trial_division(n):
    d = defaultdict(int)
    while n%2 == 0:
        d[2] += 1
        n = n//2
    p = 3
    while p**2 <= n:
        while n%p == 0:
            d[p] += 1
            n = n//p
        p += 2
    if n != 1:
        d[n] += 1
    return d

x = primes(10**6+1)
a = calc_gcd(A)
d_prime = dict()
for x0 in x:
    d_prime[x0] = 0

if a != 1:
    print('not coprime')
else:
    flag = False
    for i in range(N):
        d = trial_division(A[i])
        for k in d.keys():
            if d_prime[k]:
                flag = True
                break
            else:
                d_prime[k] += 1
        if flag:
            break
    if not flag:
        print('pairwise coprime')
    else:
        print('setwise coprime')