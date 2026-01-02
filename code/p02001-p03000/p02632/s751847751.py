MOD = int(1e9) + 7
MAX = int(2e6) + 7


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


def main():
    K = int(input())
    S = input()
    N = len(S)
    pow25 = [1] * (K+1)
    pow26 = [1] * (K+1)
    for i in range(K):
        pow25[i+1] = (pow25[i] * 25) % MOD
        pow26[i+1] = (pow26[i] * 26) % MOD
    ans = 0
    for m in range(N, N+K+1):
        tmp = (combination(m-1, N-1) * pow25[m-N] * pow26[N+K-m]) % MOD
        ans = (ans + tmp) % MOD
    print(ans)


if __name__ == "__main__":
    main()
