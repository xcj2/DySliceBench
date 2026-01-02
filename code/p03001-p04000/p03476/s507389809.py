from collections import deque
import sys
input = sys.stdin.readline
import bisect as bi
from operator import mul
from functools import reduce
import math
from itertools import accumulate

def readlines(n):
    for _ in range(n):
        a, b = map(int, input().split())
        yield a, b

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

def main():
    q = int(input())
    is_prime = prime(10**5)

    def p(total, x):
        return total + (1 if is_prime[x] and is_prime[(x+1)//2] else 0)

    cumsum = list(accumulate(range(10**5), p))
    for l, r in readlines(q):
        print(cumsum[r] - cumsum[l-1])


main()
