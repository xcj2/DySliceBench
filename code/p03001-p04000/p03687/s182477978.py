import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))
def MIIZ(): return list(map(lambda x: x-1, MII()))
## dp ##
def DD2(d1,d2,init=0): return [[init]*d2 for _ in range(d1)]
def DD3(d1,d2,d3,init=0): return [DD2(d2,d3,init) for _ in range(d1)]
## math ##
def divc(x,y) -> int: return -(-x//y)
def divf(x,y) -> int: return x//y
def gcd(x,y):
    while y: x,y = y,x%y
    return x
def lcm(x,y): return x*y//gcd(x,y)
def enumerate_divs(n):
    """Return a tuple list of divisor of n"""
    return [(i,n//i) for i in range(1,int(n**0.5)+1) if n%i==0]
def get_primes(n=10**3):
    """Return a list of prime numbers n or less"""
    is_prime = [True]*(n+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if not is_prime[i]: continue
        for j in range(i*2, n+1, i): is_prime[j] = False
    return [i for i in range(n+1) if is_prime[i]]
def prime_factor(n):
    """Return a list of prime factorization numbers of n"""
    res = []
    for i in range(2,int(n**0.5)+1):
        while n%i==0: res.append(i); n //= i
    if n != 1: res.append(n)
    return res
## const ##
MOD=10**9+7
## libs ##
import itertools as it
import functools as ft
from collections import deque, Counter
from heapq import heapify, heappop, heappush
from bisect import bisect_left
import string
#======================================================#
def main():
    s = IS()
    n = len(s)
    sc = set(s)
    ans = 10**9
    for c in string.ascii_lowercase:
        if c not in sc: continue
        cnt = 0
        t = s
        for l in range(n):
            u = ''
            if set(t) == {c}: break
            for i in range(len(t)-1):
                if t[i] == c or t[i+1] == c:
                    u += c
                else:
                    u += t[i]
            cnt += 1
            t = u
        ans = min(cnt, ans)
    print(ans)



if __name__ == '__main__':
    main()