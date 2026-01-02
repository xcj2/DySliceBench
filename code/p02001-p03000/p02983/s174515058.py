#!/usr/bin/env python
# coding: utf-8

import fractions

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

def calc(n, x):
    return n // x

def lcm(a, b):
    return (a * b) // fractions.gcd(a, b)

def main():
    l, r = rli()
    mod = [[None for _ in range(2019)] for _ in range(2019)]
    for i in range(2019):
        for j in range(i+1, 2019):
            mod[i][j] = i*j % 2019
    if r - l >= 2019:
        print(0)
        return
    l_mod = l % 2019
    r_mod = r % 2019
    if l_mod < r_mod:
        cand = list(range(l_mod, r_mod+1))
    else:
        cand = list(range(l_mod, 2019)) + list(range(0, r_mod+1))
    ans = 2018
    for i in cand:
        for j in cand:
            if i >= j:
                continue
            ans = min(ans, mod[i][j])
    print(ans)



if __name__ == '__main__':
    main()
