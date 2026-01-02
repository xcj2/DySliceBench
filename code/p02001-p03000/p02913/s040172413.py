# -*- coding: utf-8 -*-
import sys
from collections import Counter, defaultdict
buff_readline = sys.stdin.buffer.readline
readline = sys.stdin.readline


class RollingHash():
    """
    Original code is https://tjkendev.github.io/procon-library/python/string/rolling_hash.html
    """
    class RH():
        def __init__(self, s, base, mod):
            self.base = base
            self.mod = mod
            self.rev = pow(base, mod-2, mod)

            l = len(s)
            self.h = h = [0]*(l+1)
            tmp = 0
            for i in range(l):
                num = ord(s[i])
                tmp = (tmp*base + num) % mod
                h[i+1] = tmp

            self.pw = pw = [1]*(len(s)+1)
            v = 1
            for i in range(l):
                pw[i+1] = v = v * base % mod

        def calc(self, l, r):
            return (self.h[r] - self.h[l] * self.pw[r-l]) % self.mod

    @staticmethod
    def gen(a, b, num):
        result = set()
        while 1:
            import random
            import math
            random.seed()
            while 1:
                v = random.randint(a, b)//2*2+1
                if v not in result:
                    break
            for x in range(3, int(math.sqrt(v))+1, 2):
                if v % x == 0:
                    break
            else:
                result.add(v)
                if len(result) == num:
                    break
        return result

    def __init__(self, s, rand=False, num=5):
        if rand:
            bases = RollingHash.gen(2, 10**3, num)
        else:
            assert num <= 10
            bases = [641, 103, 661, 293, 547, 311, 29, 457, 613, 599][:num]

        MOD = 10**9+7
        self.rhs = [self.RH(s, b, MOD) for b in bases]

    def calc(self, l, r):
        return tuple(rh.calc(l, r) for rh in self.rhs)


class Bisect:
    def __init__(self, func):
        self.__func = func

    def bisect_left(self, x, lo, hi):
        while lo < hi:
            mid = (lo+hi)//2
            if self.__func(mid) < x:
                lo = mid+1
            else:
                hi = mid
        return lo

    def bisect_right(self, x, lo, hi):
        while lo < hi:
            mid = (lo+hi)//2
            if x < self.__func(mid):
                hi = mid
            else:
                lo = mid+1
        return lo


def slv(N, S):
    srh = RollingHash(S)

    def f(m):
        h2i = defaultdict(list)
        for i in range(N-m+1):
            h2i[srh.calc(i, i+m)].append(i)

        for l in h2i.values():
            n = l[-1] - l[0]
            if n >= m:
                return 0
        return 1

    return Bisect(f).bisect_right(0, 1, N//2+1) - 1


def main():
    N = int(input())
    S = input()
    print(slv(N, S))


if __name__ == '__main__':
    main()
