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
        query = input().split()
        yield iter(query)

def main():
    a = input().strip()
    q = int(input())

    deq = deque(a)
    first = True
    initial = True
    for query in readlines(q):
        t = next(query)
        if t == '1':
            if first:
                continue
            initial = not initial
            continue

        f, c = query
        if initial:
            if f == '1':
                deq.appendleft(c)
            else:
                deq.append(c)
        else:
            if f == '1':
                deq.append(c)
            else:
                deq.appendleft(c)

        first = False

    print("".join(deq) if initial else "".join(reversed(deq)))



main()