#!/usr/bin/env python3

import math
def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x

def fact(n):
    r = [1]
    if n % 2 == 0:
        r.append(2)
        while n % 2 == 0:
            n //= 2
    i = 3
    k = int(math.sqrt(n))
    while i <= k:
        if n % i == 0:
            r.append(i)
            while n % i == 0:
                n //= i
            k = int(math.sqrt(n))
        i += 2
    if n > 1:
        r.append(n)
    return r

def main():
    A, B = map(int, input().split())
    t = gcd(A, B)
    print(len(fact(t)))


if __name__ == '__main__':
    main()
