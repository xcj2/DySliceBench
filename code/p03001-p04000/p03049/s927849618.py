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
def to_bin(x: int) -> str: return format(x, 'b') # rev => int(res, 2)
def to_oct(x: int) -> str: return format(x, 'o') # rev => int(res, 8)
def to_hex(x: int) -> str: return format(x, 'x') # rev => int(res, 16)
MOD=10**9+7
def divc(x,y) -> int: return -(-x//y)
def divf(x,y) -> int: return x//y
def gcd(x,y):
    while y: x,y = y,x%y
    return x
def lcm(x,y): return x*y//gcd(x,y)
def enumerate_divs(n):
    """Return a tuple list of divisor of n"""
    return [(i,n//i) for i in range(1,int(n**0.5)+1) if n%i==0]
def get_primes(MAX_NUM=10**3):
    """Return a list of prime numbers n or less"""
    is_prime = [True]*(MAX_NUM+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(MAX_NUM**0.5)+1):
        if not is_prime[i]: continue
        for j in range(i*2, MAX_NUM+1, i): is_prime[j] = False
    return [i for i in range(MAX_NUM+1) if is_prime[i]]
def prime_factor(n):
    """Return a list of prime factorization numbers of n"""
    res = []
    for i in range(2,int(n**0.5)+1):
        while n%i==0: res.append(i); n //= i
    if n != 1: res.append(n)
    return res
## libs ##
from itertools import accumulate as acc, combinations as combi, product, combinations_with_replacement as combi_dup
from collections import deque, Counter
from heapq import heapify, heappop, heappush
from bisect import bisect_left
#======================================================#

def main():
    n = II()
    ss = [IS() for i in range(n)]
    ab_type = {}
    ab_type['_ab_'] = 0
    ab_type['b__a'] = 0
    ab_type['___a'] = 0
    ab_type['b___'] = 0
    for s in ss:
        for i in range(len(s)-1):
            if s[i:i+2] == 'AB':
                ab_type['_ab_'] += 1
        if s[0] == 'B' and s[-1] == 'A':
            ab_type['b__a'] += 1
        elif s[-1] == 'A':
            ab_type['___a'] += 1
        elif s[0] == 'B':
            ab_type['b___'] += 1
    cnt = 0
    cnt += ab_type['_ab_']
    if ab_type['b__a'] > 0:
        cnt += ab_type['b__a']-1
        if ab_type['___a'] > 0:
            cnt += 1
            ab_type['___a'] -= 1
        if ab_type['b___'] > 0:
            cnt += 1
            ab_type['b___'] -= 1
    cnt += min(ab_type['___a'], ab_type['b___'])
    print(cnt)

if __name__ == '__main__':
    main()