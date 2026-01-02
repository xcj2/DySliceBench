# -*- coding: utf-8 -*-
n = int(input())
al = list(map(int, input().split()))
MOD = 10**9 + 7

# aのmod Mでの逆元
def modinv(a, m):
    b = m
    u = 1
    v = 0
    while b:
        t = a//b
        a -= t*b
        a,b = b,a
        u -= t*v
        u,v = v,u
    u %= m
    if u<0:
        u += m
    return u

# GCD
def gcd(a,b):
    while b!=0:
        a,b = b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

def lcmlist(l):
    res = l[0]
    for x in l[1:]:
        res = lcm(res, x)
    return res

l = lcmlist(al)%MOD
res = 0
for a in al:
    res += l*modinv(a,MOD)
    res %= MOD

print(res)