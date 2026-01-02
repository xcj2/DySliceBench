#import sys
# import math

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

N = int(input())
#A, B = list(map(int,input().split()))
S = [''.join(sorted(input())) for _ in range(N)]
D = {}
for s in S :
    if s in D :
        D[s] += 1
    else :
        D[s] = 1
V = list(D.values())

count = 0
for v in V :
    if v == 1 :
        count += 0
    elif v == 2 :
        count += 1
    elif v >= 3 :
        count += modc(v, 2, 2 ** 63 - 1)
print(count)