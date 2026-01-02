#import heapq
import itertools
import math
#import numpy as np
import sys

def modc(a, b, m):
    c = 1
    for i in range(b):
        c = c * (a - i) % m
        c = c * modinv(i + 1, m) % m
    return c

def egcd(a, b):
    (x, lastx) = (0, 1)
    (y, lasty) = (1, 0)
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lastx) = (lastx - q * x, x)
        (y, lasty) = (lasty - q * y, y)
    return (lastx, lasty, a)

def modinv(a, m):
    (inv, q, gcd_val) = egcd(a, m)
    return inv % m

#N = int(input())
X, Y = list(map(int, input().split()))
#S = [input() for _ in range(H)]
#T = [list(map(int,input().split())) for _ in range(N)]
#sys.exit()

if (X + Y) % 3 != 0 :
    print(0)
    sys.exit()

n = int((2 * Y - X) / 3)
m = int((2 * X - Y) / 3)

if n < 0 or m < 0 :
    print(0)
    sys.exit()

ans = modc(n + m, n, 10 ** 9 + 7)
print(ans)