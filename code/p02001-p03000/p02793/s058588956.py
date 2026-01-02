#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)

MOD = 1000000007  # type: int

def solve(N: int, A: "List[int]"):
    def factorize(n):
        ret = {}
        d = 2
        mx = int(n ** 0.5) + 1
        while d < mx:
            if n % d == 0:
                ret[d] = 0
            while n % d == 0:
                ret[d] += 1
                n //= d
            d += 1
        if n > 1:
            if n not in ret:
                ret[n] = 1
            else:
                ret[n] += 1
        return ret
    divs = {}
    cur = 1
    ret = 0
    for val in A:
        facs = factorize(val)
        tmp = 1
        for k, cnt in facs.items():
            if not k in divs:
                divs[k] = 0
            if divs[k] < cnt:
                tmp *= k ** (cnt - divs[k])
                divs[k] = cnt
        cur *= tmp
        ret *= tmp
        ret += cur // val
        ret %= MOD
        #print(tmp, cur)
        #print(divs)
        #print(ret)
        #print('-------')
    print(ret)
    return ret

def solve_(N: int, A: "List[int]"):
    def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)
    g = A[0]
    for v in A:
        tmp = gcd(g, v)
        g = g * v // tmp
    ret = 0
    for v in A:
        ret += g // v
        ret %= MOD
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
