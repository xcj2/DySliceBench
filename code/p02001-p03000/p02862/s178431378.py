from math import factorial
import sys

x, y = map(int, input().split())

maxim = 10**6+10
mod = 10**9 + 7

fac = [None] * maxim
finv = [None] * maxim
inv = [None] * maxim

def cominit():
    fac[0], fac[1] = 1, 1
    finv[0], finv[1] = 1, 1
    inv[1] = 1

    for i in range(2, maxim):
        fac[i] = fac[i-1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i-1] * inv[i] % mod

def com(n, k):
    if (n < k):
        return 0
    if (n < 0 or k < 0):
        return 0
    return fac[n] * (finv[k] * finv[n - k] % mod) % mod


def main():
    if (x + y) % 3 != 0:
        return 0
    else:

        b = (2*y - x) // 3 
        a = b + x -y
        if a < 0 or b < 0:
            print(0)
            sys.exit()
        
        cominit()
        ans = com(a+b, b)
        return ans 
    # answer = (a+b)! / a!b! mod 10^9+7


    
print(main())

# 999999 999999