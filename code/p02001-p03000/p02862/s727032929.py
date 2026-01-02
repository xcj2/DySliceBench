MOD = 1000000007
MAX = 10**6  # max n

fac = [0 for _ in range(MAX)]  # = n! (mod MOD)
finv = [0 for _ in range(MAX)]  # = 1/r! (mod MOD)
inv = [0 for _ in range(MAX)]  # = 1/r (mod MOD)


# init
def COMinit():
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD


# nCk, n < [0, MAX), k < [0, n]
def COM(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD

def main():
    # input
    x, y = map(int, input().split())
    if (x+y)%3 == 0:
        num = (x+y)//3
        for i in range(num+1):
            if i + 2*(num-i) == x and 2*i + (num-i) == y:
                break
        else:
            print(0)
            return
    else:
        print(0)
        return

    # calc
    COMinit()
    print(COM(num, i))


if __name__ == '__main__':
    main()
