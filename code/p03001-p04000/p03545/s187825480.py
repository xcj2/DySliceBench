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
        for j in range(i*2, MAX_NUM+1, i):
            is_prime[j] = False
    return [i for i in range(MAX_NUM+1) if is_prime[i]]
## libs ##
from itertools import accumulate as acc
from collections import deque, Counter
from heapq import heapify, heappop, heappush
from bisect import bisect_left

#======================================================#

def main():
    a, *bcd = list(map(int, IS()))
    for bit in range(1<<3):
        sumv = a
        pm = []
        for i in range(3):
            if bit & (1<<i):
                sumv += bcd[i]
                pm.append('+')
            else:
                sumv -= bcd[i]
                pm.append('-')
        if sumv == 7:
            a = str(a)
            b = str(bcd[0])
            c = str(bcd[1])
            d = str(bcd[2])
            print(a+pm[0]+b+pm[1]+c+pm[2]+d+'=7')
            return None

if __name__ == '__main__':
    main()