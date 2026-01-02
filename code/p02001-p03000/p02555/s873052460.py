#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=tf-8
#

"""
"""

from collections import defaultdict
import bisect

import sys
input = sys.stdin.readline

modulo = (10**9)+7

P = 10**9 + 7
N = 5000
fact = [1]+[1]
for i in range(2,N):
    ff = fact[-1]*i%P
    fact.append(ff)

cut = 10**9+7


# a*s0+b*t0 = r0 = gcd(a,b)
def extendedGCD(a, b, divmod=divmod):
    r0, r1, s0, s1, t0, t1 = a, b, 1, 0, 0, 1
    while r1 != 0:
        q, rtmp = divmod(r0, r1)
        stmp, ttmp = s0-q*s1, t0-q*t1
        r0, s0, t0 = r1, s1, t1
        r1, s1, t1 = rtmp, stmp, ttmp
    return r0, s0, t0

# a*s0+b*t0 = r0 = gcd(a,b), k is the number of the steps
def extendedGCDcount(a, b, divmod=divmod):
    r0, r1, s0, s1, t0, t1 = a, b, 1, 0, 0, 1
    k = 0
    while r1 != 0:
        q, rtmp = divmod(r0, r1)
        stmp, ttmp = s0-q*s1, t0-q*t1
        r0, s0, t0 = r1, s1, t1
        r1, s1, t1 = rtmp, stmp, ttmp
        k += 1
    return r0, s0, t0, k


# the inverse of a in F_b when b is a prime
def modInverse(a, b, divmod=divmod):
    r0, r1, s0, s1 = a, b, 1, 0
    while r1 != 0:
        q, rtmp = divmod(r0, r1)
        stmp = s0-q*s1
        r0, s0 = r1, s1
        r1, s1 = rtmp, stmp
    return s0 % b

def solve(s):
    ans = 0
    for i in range(1,s//3+1):
        s2 = s-i*3 
        tmp = fact[s2+i-1]*modInverse(fact[s2],P)%P
        tmp = tmp*modInverse(fact[i-1],P)%P
        ans = (ans+tmp)%P
    print(ans)
            

def main():
    s = int(input())
    solve(s)


if __name__ == "__main__":
    main()