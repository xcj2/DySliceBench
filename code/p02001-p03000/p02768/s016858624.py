import sys
sys.setrecursionlimit(4100000)

n, a, b = map(int, input().split())
mod = 10 ** 9 + 7

#繰り返し2乗法
def  mod_pow(a:int, b:int, mod:int)->int:
    if b % 2 == 0:
        return (mod_pow(a, b//2, mod) ** 2) % mod
    elif b == 1:
        return a % mod
    else:
        return ((mod_pow(a, b//2, mod) ** 2) * a) % mod

#逆元を求める関数
def mod_inverse(mod:int, b:int)->int:
    return mod_pow(b, mod-2, mod)

#aCbをmodで割った余りを求める関数(bが小さい)
def nCr_mod(n:int, r:int, mod:int)->int:
    num, den = 1, 1 #numerator, denominator

    for i in range(r):
        num = (num * (n-i)) % mod
        den = (den * (i+1)) % mod

    return (num * mod_inverse(mod, den)) % mod
    
ans = (mod_pow(2, n, mod) - 1 - nCr_mod(n, a, mod) - nCr_mod(n, b, mod)) % mod
print(ans)