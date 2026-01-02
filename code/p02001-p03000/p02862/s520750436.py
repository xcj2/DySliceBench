import sys
MOD = 10**9 + 7

def mod_inv(n, m):
    return pow(n, m-2, m)

def nCr_mod_m(n, r, m):
    if r < 0 or n < r:
        return 0
    # n!
    fact = fact_prev = 1 # 0! = 1! = 1
    for i in range(2, n+1):
        fact = fact_prev * i % m
        fact_prev = fact
    # n!^(-1)
    fact_inv = [0]*(max(r, n-r)+1)
    fact_inv[0] = fact_inv[1] = 1  # 1 = 1 mod m
    for i in range(2, max(r, n-r)+1):
        fact_inv[i] = fact_inv[i-1] * mod_inv(i, m) % m
    return (fact * fact_inv[r] % m) * fact_inv[n-r] % m

def main():
    X, Y = map(int, input().split())
    if ((X+Y)%3 != 0) or (min(X,Y)*2 < max(X,Y)):
        print(0)
        sys.exit()

    base = (X + Y) // 3
    x = X - base
    y = Y - base

    print(nCr_mod_m(x+y, x, MOD))
main()