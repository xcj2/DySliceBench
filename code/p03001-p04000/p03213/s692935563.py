#!/usr/bin/env python3

from functools import lru_cache

def prime_factor_of_fact(n):
    di = {}
    for i in range(1, n + 1):
        pf = prime_factor(i)
        for p in pf:
            if p not in di:
                di[p] = 1
            else:
                di[p] += 1
    return di

@lru_cache()
def prime_factor(n):
    if n == 1:
        return []
    for i in range(2, n + 1):
        if n % i == 0:
            res = prime_factor(n // i) + [i]
            break
    return res

def shichigo_su(pff):
    have_seventyfour = len([k for k in pff if pff[k] >= 74])
    have_twentyfour = len([k for k in pff if pff[k] >= 24])
    have_fourteen = len([k for k in pff if pff[k] >= 14])
    have_four = len([k for k in pff if pff[k] >= 4])
    have_two = len([k for k in pff if pff[k] >= 2])
    if have_four >= 2 and have_two >= 3:
        res = ((have_four * (have_four - 1)) // 2) * (have_two - 2) \
            + have_fourteen * (have_four - 1) \
            + have_twentyfour * (have_two - 1) \
            + have_seventyfour
        return res
    else:
        return 0

def main():
    n = int(input())
    pff = prime_factor_of_fact(n)
    print(shichigo_su(pff))

main()
