import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))
def MIIZ(): return list(map(lambda x: x-1, MII()))
## dp ##
INIT_VAL = 0
def DD2(d1,d2): return [[INIT_VAL]*d2 for _ in range(d1)]
def DD3(d1,d2,d3): return [DD2(d2,d3) for _ in range(d1)]
## math ##
MOD=10**9+7
def divc(x,y): return -(-x//y)
def divf(x,y): return x//y
def gcd(x,y):
    while y: x,y = y,x%y
    return x
def lcm(x,y): return x*y//gcd(x,y)
def get_primes(MAX_NUM=10**3):
    """Return a list of prime numbers"""
    is_prime = [True] * MAX_NUM
    is_prime[0] = False
    is_prime[1] = False
    primes = []
    for i in range(MAX_NUM):
        if is_prime[i]:
            primes.append(i)
            for j in range(2*i, MAX_NUM, i):
                is_prime[j] = False
    return primes
## libs ##
from itertools import accumulate as acc
from collections import deque, Counter
from heapq import heapify, heappop, heappush
from bisect import bisect_left

#======================================================#

def main():
    a, b = MII()
    print(divc(a+b, 2))

if __name__ == '__main__':
    main()