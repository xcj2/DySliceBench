from heapq import heappush, heappop
from collections import deque
import re
import math
import functools
import itertools
import fractions

def sRaw():
    return input().rstrip("\r")


def iRaw():
    return int(input())


def ssRaw():
    return input().split()


def isRaw():
    return list(map(int, ssRaw()))


INF = 1 << 29


def mk1d(n, val=INF):
    return [val for i in range(n)]

def mk2d(h, w, val=INF):
    return [[val for i in range(w)]for i in range(h)]

DIV = 998244353


def convolve(a, b):
    p, g = 1107296257, 5
    n0, n1 = len(a), len(b)
    n = 1 << (max(n0, n1) - 1).bit_length() + 1
    a = a + [0] * (n-n0)
    b = b + [0] * (n-n1)
    w = pow(g, (p - 1) // n, p)
    invw = pow(w, p-2, p)

    def fft(f):
        d = n // 2
        v = w
        while d >= 1:
            u = 1
            for i in range(d):
                for j in range(i, n, 2*d):
                    f[j], f[j+d] = (f[j] + f[j+d]) % p, u * (f[j] - f[j+d]) % p
                u = u * v % p
            v = v * v % p
            d //= 2

    def ifft(f):
        d = 1
        while d < n:
            v = pow(invw, n // (2 * d), p)
            u = 1
            for i in range(d):
                for j in range(i, n, 2*d):
                    f[j+d] *= u
                    f[j], f[j+d] = (f[j] + f[j+d]) % p, (f[j] - f[j+d]) % p
                u = u * v % p
            d *= 2

    fft(a), fft(b)
    for i in range(n):
        a[i] = a[i] * b[i] % p
    ifft(a)
    invn = pow(n, p - 2, p)
    return [a[i] * invn % p for i in range(n0 + n1 - 1)]


def gcd(a, b):
    if(b == 0):
        return a
    return gcd(b, a % b)

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)


def lcm(*numbers):
    return functools.reduce(lcm_base, numbers, 1)


def lcm_list(numbers):
    return functools.reduce(lcm_base, numbers, 1)

def main():
    C = sRaw()
    
    return chr(ord(C)+1)

if __name__ == "__main__":
    print(main())
