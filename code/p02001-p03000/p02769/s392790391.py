#標準入力を高速に
import sys
input = sys.stdin.readline

def factorial_mod(x, y, mod):
    factorial = 1
    for i in range(x,y+1):
        factorial *= i
        factorial %= mod
    return factorial
  
def n_C_k(n, k, mod, fact):
    inv = (pow(fact[n-k], mod-2, mod) * pow(fact[k], mod-2, mod)) % mod
    return (fact[n] * inv) % mod

"""
#main関数(若干早くなる)
def main():
    mod = 10**9+7
    n, k = map(int, input().split())         
    ans = 1+n*(n-1)

    a = n
    b = n-1

    for i in range(1, min(n, k)):
        temp1 = (n-i)*pow(i+1, mod-2, mod)%mod
        a *= temp1
        a %= mod
        temp2 = (n-1-i)*pow(i+1, mod-2, mod)%mod
        b *= temp2
        b %= mod
        temp3 = a*b%mod
        ans += temp3
        ans %= mod

    print(ans)
"""


#main関数(若干早くなる)
def main():
    mod = 10**9+7
    n, k = map(int, input().split())
    ans = (1+n*(n-1))%mod

    #階乗を使いまわすver.
    fact = [1]*(n+1)
    for i in range(1, n+1):
        fact[i] = fact[i-1]*i
        fact[i] %= mod

    for i in range(2, min(n-1, k)+1):
        ans += n_C_k(n, i, mod, fact)*n_C_k(n-1, i, mod, fact)
        ans %= mod

    print(ans)


if __name__ == '__main__':
    main()
