MOD = 10**9 + 7
MAX = int(2e5)


def div(a, b):
    return a * pow(b, MOD-2, MOD) % MOD


FACT = [1] * (MAX+1)
for i in range(1, MAX+1):
    FACT[i] = (i * FACT[i-1]) % MOD
INV = [1] * (MAX+1)
INV[MAX] = div(1, FACT[MAX])
for i in range(MAX, 0, -1):
    INV[i-1] = (INV[i] * i) % MOD


def combi(n, x):
    ret = 1
    for i in range(x):
        ret = ret * (n-i) % MOD
    ret = ret * INV[x] % MOD
    return ret


def main():
    n, a, b = map(int, input().split())
    ans = pow(2, n, MOD) - 1
    ans = (ans - combi(n, a) - combi(n, b)) % MOD
    print(ans)


if __name__ == "__main__":
    main()
