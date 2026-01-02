import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

N = int(input())
A = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
def lcm(a, b):
    return (a * b // gcd(a, b))

l = A[0]
for i in range(1, N):
    l = lcm(l, A[i])

def my_pow(base, n, mod):
    if n == 0:
        return 1
    x = base
    y = 1
    while n > 1:
        if n % 2 == 0:
            x *= x
            n //= 2
        else:
            y *= x
            n -= 1
        x %= mod
        y %= mod
    return x * y % mod

ans = 0
for a in A:
    ans += my_pow(a, MOD - 2, MOD)
print((ans * l)% MOD)