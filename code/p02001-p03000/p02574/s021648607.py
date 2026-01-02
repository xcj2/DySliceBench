import sys
input = sys.stdin.readline
from collections import defaultdict
from functools import reduce
N = int(input())
A = list(map(int,input().split()))

def gcd(a,b):
    while b:
        a,b = b, a%b
    return a

def sieve_Eratosthenes(n):
    f = [True]*(n+1)
    f[0] = False
    f[1] = False
    m = int(n**0.5+1)
    for i in range(2,m):
        if f[i]:
            for j in range(i*i,n+1, i):
                f[j] = False
    return f

def getPrimeLists(n):
    table = sieve_Eratosthenes(n)
    return [x for x in range(2,n+1) if table[x]]

def primeFactorization(n):
    res = defaultdict(int)
    m = int(n**0.5)
    for i in range(2,m+1):
        while n % i == 0:
            n = n//i
            res[i] += 1
    if n > 1:
        res[n] = 1
    return res

table = [0] * (10**6+10)
f = False
for a in A:
    pf = primeFactorization(a).keys()
    for p in pf:
        if table[p] > 0:
            f = True
        table[p] += 1
    if f:
        break
else:
    print('pairwise coprime')
    exit()

allgcd = reduce(gcd, A)
if allgcd == 1:
    print('setwise coprime')
    exit()

print('not coprime')
