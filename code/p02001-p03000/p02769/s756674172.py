#!/bin/bash
''':'
docker run --rm -it -v $(cd $(dirname $0) && pwd):/vo:ro pypy:3-2.4.0 \
   /bin/bash -c "pypy3 /vo/$(basename $0) < /vo/g.inp"
exit $?
'''
import sys


def _ia(): return [int(x) for x in sys.stdin.readline().strip().split()]


MOD = 10**9 + 7


def add(a, b):
    return (a+b) % MOD


def mul(a, b):
    return (a*b) % MOD


def pow(a, n):
    ret = 1
    an = a
    while n > 0:
        if n & 1 == 1:
            ret = (ret * an) % MOD
        an = (an * an) % MOD
        n >>= 1
    return ret


def div(a, b):
    if a % b == 0:
        return a//b
    return (a * pow(b, MOD-2)) % MOD


def comb(n, k):
    global fact, ifact
    if k == 0:
        return 1
    return mul(mul(fact[n], ifact[n-k]), ifact[k])


n, k = _ia()
k = min(n-1, k)

fact = [1] * (n+1)
ifact = [1] * (n+1)
for i in range(1, n+1):
    fact[i] = mul(i, fact[i-1])
    ifact[i] = div(ifact[i-1], i)

ret = 0
for i in range(k+1):
    ret = (ret + comb(n-1, i) * comb(n, i)) % MOD
print(ret)
