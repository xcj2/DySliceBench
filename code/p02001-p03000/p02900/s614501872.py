import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools, os, pdb
sys.setrecursionlimit(10**7)
from queue import PriorityQueue
inf = 10 ** 20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def _I(): return int(sys.stdin.readline())
def _F(): return float(sys.stdin.readline())
def _pf(s): return print(s, flush=True)
def perr(s): return print(s, file=sys.stderr)
"""
互いに素な整数の組を選ぶ
A.Bの公約数は
12 18なら
1, 2, 3, 6
ってやっていくと無理がある
そもそも約数がある時点でだめでは？

"""

A, B = LI()
if A == B == 1:
    print(1)
    exit()
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    print(a)
    return a

def cf(x1,x2):
    cf=[]
    for i in range(2,min(x1,x2)+1):
        if x1 % i == 0 and x2 % i == 0:
            cf.append(i)
    return cf

def get_sieve_of_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = [2]
    limit = int(n**0.5)
    data = [i + 1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr
A_fac = factorization(A)
B_fac = factorization(B)
perr(A_fac)
perr(B_fac)
ans = 1
b_fac = [b[0] for b in B_fac]
for a in A_fac:
    if a[0] in b_fac:
        ans += 1
#  for a, b in zip(A_fac, B_fac):
#      if a[0] == b[0]:
#          ans += 1

print(ans)
