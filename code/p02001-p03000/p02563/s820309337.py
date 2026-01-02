# Date [ 2020-09-11 01:37:51 ]
# Problem [ f.py ]
# Author Koki_tkg
# もう少し整理したら使いやすくなりそう

# convolution.py
def butterfly(a: list):
    n = len(a)
    h = ceil_pow2(n)
    g = primitive_root(MOD)
    
    first = True
    sum_e = [0] * 30
    if first:
        first = False
        es = [0] * 30; ies = [0] * 30
        cnt2 = bsf(MOD - 1)
        e = pow_(g, (MOD - 1) >> cnt2); ie = inv(e, MOD)
        for i in range(cnt2, 1, -1):
            es[i - 2] = e
            ies[i - 2] = ie
            e = e * e % MOD
            ie = ie * ie % MOD
        now = 1
        for i in range(cnt2 - 2):
            sum_e[i] = es[i] * now % MOD
            now = now * ies[i] % MOD
    for ph in range(1, h + 1):
        w = 1 << (ph - 1); p = 1 << (h - ph)
        now = 1
        for s in range(w):
            offset = s << (h - ph + 1)
            for i in range(p):
                l = a[i + offset] % MOD
                r = a[i + offset + p] * now % MOD
                a[i + offset] = (l + r) % MOD
                a[i + offset + p] = (l - r) % MOD
            now = now * sum_e[bsf(~s)] % MOD
    return a

def butterfly_inv(a: list):
    n = len(a)
    h = ceil_pow2(n)
    g = primitive_root(MOD)
    
    first = True
    sum_ie = [0] * 30
    if first:
        first = False
        es = [0] * 30; ies = [0] * 30
        cnt2 = bsf(MOD - 1)
        e = pow_(g, (MOD - 1) >> cnt2) % MOD; ie = inv(e, MOD) % MOD
        for i in range(cnt2, 1, -1):
            es[i - 2] = e
            ies[i - 2] = ie
            e = e * e % MOD
            ie = ie * ie % MOD
        now = 1
        for i in range(cnt2 - 2):
            sum_ie[i] = ies[i] * now % MOD
            now = es[i] * now % MOD
    for ph in range(h, 0, -1):
        w = 1 << (ph - 1); p = 1 << (h - ph)
        inow = 1
        for s in range(w):
            offset = s << (h - ph + 1)
            for i in range(p):
                l = a[i + offset] % MOD
                r = a[i + offset + p] % MOD
                a[i + offset] = (l + r) % MOD
                a[i + offset + p] = (MOD + l - r) * inow % MOD
            inow = sum_ie[bsf(~s)] * inow % MOD
    return a
    
def convolution(a: list, b: list):
    n = len(a); m = len(b)
    if not n or not m: return []
    if min(n, m) <= 60:
        if n < m:
            n, m = m, n
            a, b = b, a
        ans = [0] * (n + m - 1)
        for i in range(n):
            for j in range(m):
                ans[i + j] += a[i] * b[j] % MOD
                ans[i + j] %= MOD
        return ans
    z = 1 << ceil_pow2(n + m - 1)
    a = a + [0] * (z - len(a))
    a = butterfly(a)
    b = b + [0] * (z - len(b))
    b = butterfly(b)
    for i in range(z):
        a[i] *= b[i]
        a[i] %= MOD
    a = butterfly_inv(a)
    a = a[:n + m - 1]
    iz = inv(z, MOD)
    for i in range(n + m - 1):
        a[i] *= iz
        a[i] %= MOD
    return a

def inv(x, m):
    if is_prime_constexpr(m):
        assert x
        return pow_(x, m - 2)
    else:
        eg = inv_gcd(x, m)
        assert eg[0] == 1
        return eg[2]

def pow_(x, n: int):
    assert 0 <= n
    r = 1
    while n:
        if n & 1: r = r*x%MOD
        x = x*x%MOD
        n >>= 1
    return r

def inv_gcd(a: int, b: int) -> tuple:
    a = safe_mod(a, b)
    if a == 0: return (b, 0)
    s = b; t = a; m0 = 0; m1 = 1
    while t:
        u = s // t
        s -= t * u
        m0 -= m1 * u
        tmp = s; s = t; t = tmp; tmp = m0; m0 = m1; m1 = tmp
    if m0 < 0: m0 += b // s
    return (s, m0)

def is_prime_constexpr(n: int) -> bool:
    if n <= 1: return False
    if n == 2 or n == 7 or n == 61: return True
    if n % 2 == 0: return False
    d = n - 1
    while d % 2 == 0: d //= 2
    for a in [2, 7, 61]:
        t = d
        y = pow_mod_constexpr(a, t, n)
        while t != n - 1 and y != 1 and y != n - 1:
            y = y * y % n
            t <<= 1
        if y != n - 1 and t % 2 == 0: return False
    return True

def pow_mod_constexpr(x: int, n: int, m: int) -> int:
    if m == 1: return 0
    _m = m; r = 1; y = safe_mod(x, m)
    while n:
        if n & 1: r = (r * y) % _m
        y = (y * y) % _m
        n >>= 1
    return r

# internal_math.py
def safe_mod(x: int, m: int) -> int:
    x %= m
    if x < 0: x += m
    return x

class barrett:
    def __init__(self, m: int):
        self._m = m
        self.im = -1 // (m + 1)
    def umod(self): return self._m
    def mul(self, a: int, b: int) -> int:
        z = a
        z *= b
        x = (z * im) >> 64
        v = z - x * self._m
        if self._m <= v: v += self._m
        return v        

def pow_mod_constexpr(x: int, n: int, m: int) -> int:
    if m == 1: return 0
    _m = m; r = 1; y = safe_mod(x, m)
    while n:
        if n & 1: r = (r * y) % _m
        y = (y * y) % _m
        n >>= 1
    return r

def is_prime_constexpr(n: int) -> bool:
    if n <= 1: return False
    if n == 2 or n == 7 or n == 61: return True
    if n % 2 == 0: return False
    d = n - 1
    while d % 2 == 0: d //= 2
    for a in [2, 7, 61]:
        t = d
        y = pow_mod_constexpr(a, t, n)
        while t != n - 1 and y != 1 and y != n - 1:
            y = y * y % n
            t <<= 1
        if y != n - 1 and t % 2 == 0: return False
    return True
def is_prime(n: int) -> bool: return is_prime_constexpr(n)

def inv_gcd(self, a: int, b: int) -> tuple:
    a = safe_mod(a, b)
    if a == 0: return (b, 0)
    s = b; t = a; m0 = 0; m1 = 1
    while t:
        u = s // t
        s -= t * u
        m0 -= m1 * u
        tmp = s; s = t; t = tmp; tmp = m0; m0 = m1; m1 = tmp
    if m0 < 0: m0 += b // s
    return (s, m0)

def primitive_root_constexpr(m: int) -> int:
    if m == 2: return 1
    if m == 167772161: return 3
    if m == 469762049: return 3
    if m == 754974721: return 11
    if m == 998244353: return 3
    divs = [0] * 20
    divs[0] = 2
    cnt = 1
    x = (m - 1) // 2
    while x % 2 == 0: x //= 2
    i = 3
    while i * i <= x:
        if x % i == 0:
            divs[cnt] = i; cnt += 1
            while x % i == 0:
                x //= i
        i += 2
    if x > 1: divs[cnt] = x; cnt += 1
    g = 2
    while True:
        ok = True
        for i in range(cnt):
            if pow_mod_constexpr(g, (m - 1) // div[i], m) == 1:
                ok = False
                break
        if ok: return g
        g += 1

def primitive_root(m: int) -> int: return primitive_root_constexpr(m)

# internal_bit.py
def ceil_pow2(n: int) -> int:
    x = 0
    while (1 << x) < n: x += 1
    return x

def bsf(n: int) -> int:
    return (n & -n).bit_length() - 1

import sys
# import math
# import bisect
# import numpy as np
# from decimal import Decimal
# from numba import njit, i8, u1, b1 #JIT compiler
# from itertools import combinations, product
# from collections import Counter, deque, defaultdict

# sys.setrecursionlimit(10 ** 6)
MOD = 998244353
INF = 10 ** 9
PI = 3.14159265358979323846

def read_str():      return sys.stdin.readline().strip()
def read_int():      return int(sys.stdin.readline().strip())
def read_ints():     return map(int, sys.stdin.readline().strip().split())
def read_ints2(x):   return map(lambda num: int(num) - x, sys.stdin.readline().strip().split())
def read_str_list(): return list(sys.stdin.readline().strip().split())
def read_int_list(): return list(map(int, sys.stdin.readline().strip().split()))
def GCD(a: int, b: int) -> int: return b if a%b==0 else GCD(b, a%b)
def LCM(a: int, b: int) -> int: return (a * b) // GCD(a, b)

def Main():
    n, m = read_ints()
    a = read_int_list()
    b = read_int_list()
    a = [x % MOD for x in a]
    b = [x % MOD for x in b]
    ans = convolution(a, b)
    print(*ans)

if __name__ == '__main__':
    Main()