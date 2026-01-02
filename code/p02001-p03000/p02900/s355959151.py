#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


A, B = list(map(int, input().split()))
# A, B = [12, 18]
# A, B = [420, 660]
# A, B = [1, 2019]


# 1. A,B の gcd を取得して C とする
# 2. C を素因数分解する
# 3. 「素因数分解の数 + 1」を返す

def gcd(a, b):
    # a の方が大きいと仮定
    def _gcd(a, b):
        # print(a, b)
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)

    if a < b:
        return _gcd(b, a)
    else:
        return _gcd(a, b)


def factorize(x):
    res = {}
    for i in range(2, int(math.sqrt(x) + 1)):  # x まで行かずともよさそう
        if x % i == 0:
            while x % i == 0:
                x //= i
                res[i] = res.get(i, 0) + 1

    if x != 1:
        res[x] = 1

    return res

C = gcd(A, B)
factors = factorize(C)
print(len(factors) + 1)
