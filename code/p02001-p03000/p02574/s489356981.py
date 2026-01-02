import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, acos, atan, asin, log, log10, gcd
from itertools import permutations, combinations, product, accumulate, combinations_with_replacement
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
#from fractions import gcd
from decimal import *
import heapq
def debug(*args):
    if debugmode:
        print(*args)
def input(): return sys.stdin.readline().strip()
def STR(): return input()
def INT(): return int(input())
def FLOAT(): return float(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 9)
inf = sys.maxsize
mod = 10 ** 9 + 7
dx = [0, 1, 0, -1, 1, -1, -1, 1]
dy = [1, 0, -1, 0, 1, -1, 1, -1]
debugmode = True

NN = 10 ** 6 + 100
primes = []
isprime = [True for _ in range(NN + 1)]
min_factor = [-1 for _ in range(NN + 1)]
#エラトステネスの篩
for i in range(2, NN + 1):
    if not isprime[i]:
        continue
    primes.append(i)
    min_factor[i] = i
    for j in range(i * 2, NN + 1, i):
        isprime[j] = False
        if min_factor[j] == -1:
            min_factor[j] = i
def prime_factorize(n):
    res = set([])
    while n != 1:
        prime = min_factor[n]
        exp = 0
        while min_factor[n] == prime:
            exp += 1
            n //= prime
        res.add(prime)
    return res

n = INT()
a = LIST()
b = []
for aa in a:
    b.append(prime_factorize(aa))
all_and = b[0]
for bb in b[1:]:
    all_and = all_and & bb
if len(all_and):
    print('not coprime')
    exit()
c = []
for bb in b:
    for tmp in bb:
        c.append(tmp)
d = set(c)
if len(c) != len(d):
    print('setwise coprime')
else:
    print('pairwise coprime')