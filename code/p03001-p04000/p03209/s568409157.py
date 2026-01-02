#!/usr/bin/env python3

from functools import lru_cache

NMAX = 50

@lru_cache(maxsize=1)
def get_sizes():
    res = [1]
    for i in range(1, NMAX + 1):
        res.append(res[-1] * 2 + 3)
    return tuple(res)

@lru_cache(maxsize=1000)
def eat_m_layers_of_level_k(k, m, si):
    assert 0 < m <= si[k]
    if k == 0:
        pats = 1
        buns = 0
    else:
        sublev = si[k - 1]
        pp, bb = eat_m_layers_of_level_k(k - 1, si[k - 1], si)
        if m == 1:
            pats = 0
            buns = 1
        elif 1 < m <= 1 + sublev:
            p, b = eat_m_layers_of_level_k(k - 1, m - 1, si)
            pats = p
            buns = b + 1
        elif m == 2 + sublev:
            pats = pp + 1
            buns = bb + 1
        elif 2 + sublev < m <= 2 + 2 * sublev:
            p, b = eat_m_layers_of_level_k(k - 1, m - si[k - 1] - 2, si)
            pats = pp + p + 1
            buns = bb + b + 1
        elif m == si[k]:
            pats = 2 * pp + 1
            buns = 2 * bb + 2
        else:
            raise ValueError
    return pats, buns

def main():
    n, x = map(int, input().split())
    si = get_sizes()
    p, b = eat_m_layers_of_level_k(n, x, si)
    print(p)

main()
