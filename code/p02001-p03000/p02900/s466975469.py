#!/usr/bin/env python3

def main():
    a, b = map(int, input().split())
    c = gcd(a, b)
    pf = prime_factor(c)
    pfu = set(pf)
    print(len(pfu) + 1)

def gcd(x, y):
    if x < y:
        x, y = y, x  # x >= y
    while y > 0:
        r = x % y
        x = y
        y = r
    return x

def prime_factor(n):
    resid = n
    result = []
    i = 2
    while True:
        if resid <= 1:
            return result
        if i ** 2 > resid:
            result.append(resid)
            return result
        if resid % i == 0:
            result.append(i)
            resid /= i
        else:
            i += 1

if __name__ == "__main__":
    main()
