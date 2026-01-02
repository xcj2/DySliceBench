from collections import deque
import sys
input = sys.stdin.readline
import bisect as bi
from operator import mul
from functools import reduce
import math

def fast_comb(a,b,mod):
    up = reduce(lambda x,y: x*y%mod, range(a,a-b,-1))
    down = reduce(lambda x,y: x*y%mod, range(1,b+1))
    return (up * pow(down, mod-2, mod)) % mod

def prime(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if not is_prime[i]:
            continue
        for j in range(i*2, n+1, i):
            is_prime[j] = False
    return is_prime

def readlines(n):
    for _ in range(n):
        map(int, input().split())
        yield

def main():
    n,a,b = map(int,input().split())

    base = (n//(a+b)) * a
    plus = min(n % (a+b), a)

    print(base + plus)

main()
