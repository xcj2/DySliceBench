MOD = 10 ** 9 + 7

def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    X, Y = ZZ()
    if (X + Y)%3 != 0:
        print(0)
        return

    N = (X + Y)//3
    if abs(X - Y) > N:
        print(0)
        return
        
    fact = [0] * (N + 1) # fact[n] = n!
    ifact = [0] * (N + 1)

    for i in range(N+1):
        if i == 0:
            fact[i] = 1
            continue
        fact[i] = i * fact[i-1]
        fact[i] %= MOD
    ifact[N] = pow(fact[N], MOD-2, MOD)
    for i in range(N)[::-1]:
        ifact[i] = ((i+1) * ifact[i+1])%MOD

    m = (2*X - Y)//3
    n = (-X + 2*Y)//3

    output = fact[m+n] * ifact[m] * ifact[n] % MOD
    print(output)

    return

if __name__ == '__main__':
    main()

