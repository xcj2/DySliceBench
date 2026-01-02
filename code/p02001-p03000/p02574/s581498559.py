import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = list(mapint())
As.sort()

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

pairwise = True
s = set()
maxi = As[-1]
for i in range(N):
    a = As[i]
    if a in s:
        pairwise = False
        break
    if a==1:
        continue
    primes = list(set(prime_factorize(a)))
    for p in primes:
        cnt = 1
        while cnt*p<=maxi:
            s.add(cnt*p)
            cnt += 1
else:
    print('pairwise coprime')
    exit()

from math import gcd
g = 0
for a in As:
    g = gcd(g, a)
if g==1:
    print('setwise coprime')
    exit()
else:
    print('not coprime')