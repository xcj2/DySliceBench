MOD = 10**9 + 7
MAX = int(5e5)


def div(a, b):
    return a * pow(b, MOD-2, MOD) % MOD


FACT = [1] * (MAX+1)
for i in range(1, MAX+1):
    FACT[i] = (i * FACT[i-1]) % MOD
INV = [1] * (MAX+1)
INV[MAX] = div(1, FACT[MAX])
for i in range(MAX, 0, -1):
    INV[i-1] = (INV[i] * i) % MOD


def combination(m, n):
    return (FACT[m] * INV[n] * INV[m-n]) % MOD


def permutation(m, n):
    return (FACT[m] * INV[m-n]) % MOD


def main():
    N, M = map(int, input().split())
    ans = 0
    for i in range(N+1):
        # 包除原理
        tmp = (combination(N, i) * permutation(M, i)
               * (permutation(M-i, N-i)**2)) % MOD
        ans = (ans + (-1)**i * tmp) % MOD

    print(ans)


if __name__ == "__main__":
    main()
