#標準入力を高速に
import sys 
input = sys.stdin.readline

def factorial_mod(x, y, mod):
    factorial = 1
    for i in range(x,y+1):
        factorial *= i
        factorial %= mod
    return factorial

def n_C_k(n,k,mod):
    factorial_nk = factorial_mod(n-k+1, n, mod)
    factorial_k = factorial_mod(1,k,mod)
    conbi=factorial_nk*pow(factorial_k, mod-2, mod)
    return conbi%mod

#main関数(若干早くなる)
def main():
    n, k = map(int, input().split())
    mod = 10**9+7
    ans = 1+n*(n-1)

    a = n
    #a = n_C_k(n, 1, mod)
    #b = n_C_k(n-1, 1, mod)
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

if __name__ == '__main__':
    main()