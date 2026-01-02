# -*- coding: utf-8 -*-
from functools import lru_cache
from itertools import permutations
import bisect
INF = 2**62-1

def read_str():
    return input().strip()

def slv(A, B, C):
    @lru_cache(maxsize=None)
    def g(x, y):
        m = []
        for i in range(len(x)):
            for j in range(min(len(y), len(x)-i)):
                if not (x[i+j] == '?' or y[j] == '?' or x[i+j] == y[j]):
                    break
            else:
                m.append(i)
        m.append(len(x))
        return m

    def f(x, y, z):
        lx = len(x)
        ly = len(y)
        lz = len(z)
        ans = lx + ly + lz
        xy = g(x, y)
        yz = g(y, z)
        xz = g(x, z)
        xz_set = set(xz)
        for i in xy:
            for j in yz:
                if i + j < lx and i + j in xz_set:
                    s = max(i + ly, i + j + lz, lx)
                elif i + j < lx and i + len(y) :
                    l = bisect.bisect_left(xz, i+ly)
                    if l >= len(xz):
                        continue
                    k = xz[l]
                    s = max(i + ly, k + len(z), len(x))
                elif  i + j >= lx:
                    s = max(i + ly, i + j + lz, lx)
                else:
                    continue
                ans = min(ans, s)
        return ans

    ans = INF
    for a, b, c in permutations((A, B, C)):
        ans = min(ans, f(a, b, c))

    return ans


def main():
    A = read_str()
    B = read_str()
    C = read_str()
    print(slv(A, B, C))



if __name__ == '__main__':
    main()
