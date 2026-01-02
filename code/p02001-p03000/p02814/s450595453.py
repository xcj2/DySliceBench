#!/usr/bin/env python3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    t = {times_divide_by_two(x) for x in a}
    if len(t) > 1:
        print(0)
        return
    l = lcm(a)
    print((m + l // 2) // l)

def times_divide_by_two(x):
    res = 0
    for i in range(200):
        if x % 2 > 0:
            return res
        res += 1
        x //= 2

def lcm(li):
    res = 1
    for x in li:
        res *= (x // gcd(res, x))
    return res

def gcd(x, y):
    if x < y:
        x, y = y, x  # x >= y
    while y > 0:
        r = x % y
        x = y
        y = r
    return x

if __name__ == "__main__":
    main()
