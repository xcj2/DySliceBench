# -*- coding: utf-8 -*-


import sys
# sys.setrecursionlimit(10**6)
# readline = sys.stdin.buffer.readline
readline = sys.stdin.readline

INF = 1 << 50


def read_int():
    return int(readline())


def read_int_n():
    return list(map(int, readline().split()))


def read_float():
    return float(readline())


def read_float_n():
    return list(map(float, readline().split()))


def read_str():
    return readline().strip()


def read_str_n():
    return readline().strip().split()


def ep(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.perf_counter()
        ret = f(*args, **kwargs)
        e = time.perf_counter()

        ep(e - s, 'sec')
        return ret

    return wrap


def divisor(n):
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            yield i
            if i != n // i:
                yield n // i


def crt(R, M):
    def exEuclid(a, mod):
        b = mod
        s, u = 1, 0
        while b:
            q = a // b
            a, b = b, a % b
            s, u = u, s - q * u
        return a, s % mod
    assert len(R) == len(M)
    r0, m0 = 0, 1
    for r, m in zip(R, M):
        assert m >= 1
        r %= m
        if m0 < m:
            r0, r = r, r0
            m0, m = m, m0
        if m0 % m == 0:
            if r0 % m != r:
                return (0, 0)
            continue
        g, im = exEuclid(m0, m)
        u = m // g
        if (r - r0) % g:
            return (0, 0)
        x = (r - r0) // g % u * im % u
        r0 += x * m0
        m0 *= u
        if r0 < 0:
            r0 += m0
    return (r0, m0)


@mt
def slv(N):
    ans = INF
    for x in divisor(2*N):
        kc, _ = crt([0, -1], (x, 2*N//x))
        if kc != 0:
            ans = min(ans, kc)
    return ans


def main():
    N = read_int()
    print(slv(N))


if __name__ == '__main__':
    main()
