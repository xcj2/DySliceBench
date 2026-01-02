import sys
import math
import functools
stdin = sys.stdin
mod = 10**9 + 7

ns = lambda: stdin.readline().rstrip()
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
sa = lambda h: [list(map(int, stdin.readline().split())) for i in range(h)]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return a * b // gcd (a, b)
def lcm_n(nums):
    return functools.reduce(lcm, nums)
def count_div2(x):
    c = 0
    while x%2 == 0:
        c += 1
        x //= 2
    return c
n, m = na()
a = na()
div2 = count_div2(a[0])
if any([count_div2(ai) != div2 for ai in a]):
    print(0)
else:
    r = lcm_n(a)//2
    b = m//r
    print((b+1)//2)
