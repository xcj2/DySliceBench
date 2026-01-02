MOD = 10**9 + 7
n, a, b = map(int, input().split())


def pow(x, n, MOD):
    res = 1
    while n:
        if n & 1:
            res *= x
            res %= MOD
        x *= x
        x %= MOD
        n >>= 1
    return res    


def fact(a, b, MOD):
    res = 1
    for i in range(a, b+1):
        res *= i
        res %= MOD
    return res


def combi(n, k, MOD):
    x = fact(n - k + 1, n, MOD)
    y = fact(1, k, MOD)
    return x * pow(y, MOD - 2, MOD) % MOD
    

def solve():
    ans = pow(2, n, MOD) - 1 - combi(n, a, MOD) - combi(n, b, MOD)
    print(ans % MOD)
    #print(pow(2, MOD, MOD))


if __name__ == "__main__":
    solve()