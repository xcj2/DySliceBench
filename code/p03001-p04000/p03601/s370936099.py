#!/usr/bin/env python3

import sys, math, copy
# import fractions, itertools
# import numpy as np
# import scipy

MOD = 10 ** 9 + 7
HUGE = 2147483647
HUGEL = 9223372036854775807
ABC = "abcdefghijklmnopqrstuvwxyz"

def main():
    def mass_water(n, m):
        return 100 * n * a + 100 * m * b

    def mass_sugar(k, l):
        return k * c + l * d

    def mass(n, m, k, l):
        return mass_water(n, m) + mass_sugar(k, l)

    def is_within_f(ms, mw):
        return ms + mw <= f

    def is_within_e(ms, mw):
        return ms * 100 <= mw * e

    def density(ms, mw):
        return ms / mw

    a, b, c, d, e, f = map(int, input().split())
    max_n = f // (100 * a)
    max_m = f // (100 * b)
    max_sugar = f * e / 100.0
    max_k = math.ceil(max_sugar // c)
    max_l = math.ceil(max_sugar // d)

    mass_water_set = set()
    for n in range(max_n + 1):
        for m in range(max_m + 1):
            mw = mass_water(n, m)
            if n + m > 0 and is_within_f(0, mw):
                mass_water_set.add(mw)
    mass_sugar_set = set()
    for k in range(max_k + 1):
        for l in range(max_l + 1):
            mass_sugar_set.add(mass_sugar(k, l))


    max_density = -HUGE
    max_mw = 0
    max_ms = 0
    for mw in mass_water_set:
        for ms in mass_sugar_set:
            if not (is_within_f(ms, mw) and is_within_e(ms, mw)):
                continue
            den = density(ms, mw)
            if den > max_density:
                max_density = den
                max_mw = mw
                max_ms = ms

    print(max_mw + max_ms, max_ms)

main()
