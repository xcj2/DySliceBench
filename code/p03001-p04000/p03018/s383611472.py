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
def to_bin(x: int) -> str: return format(x,'b') # rev => int(res, 2)
def to_oct(x: int) -> str: return format(x,'o') # rev => int(res, 8)
def to_hex(x: int) -> str: return format(x,'x') # rev => int(res, 16)
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
#======================================================#
def main():
    s = IS()
    n = len(s)
    s = s[::-1]
    cb_num = 0
    a_num = 0
    cnt = 0
    i = 0
    while i < n:
        if cb_num == 0:
            if s[i:i+2] == 'CB':
                cb_num += 1
                i += 2
                continue
        if s[i:i+2] == 'CB':
            cb_num += 1
            i += 2
        elif s[i] == 'A':
            cnt += cb_num
            i += 1
        else:
            cb_num = 0
            i += 1
    print(cnt)

if __name__ == '__main__':
    main()