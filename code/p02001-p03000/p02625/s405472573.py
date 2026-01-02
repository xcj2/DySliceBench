MOD = 10 ** 9 + 7


def prepare(n):
    global MOD
    modFacts = [0] * (n + 1)
    modFacts[0] = 1
    for i in range(n):
        modFacts[i + 1] = (modFacts[i] * (i + 1)) % MOD

    invs = [1] * (n + 1)
    invs[n] = pow(modFacts[n], MOD - 2, MOD)
    for i in range(n, 1, -1):
        invs[i - 1] = (invs[i] * i) % MOD

    return modFacts, invs


def comb(n, r):
    global MOD, modFacts, invs
    return (modFacts[n] * invs[n - r] * invs[r]) % MOD


def perm(n, r):
    global MOD, modFacts, invs
    return (modFacts[n] * invs[n - r]) % MOD


N, M = map(int, input().split())
modFacts, invs = prepare(M)
ans = 0
flag = 1
for i in range(N + 1):
    a = comb(N, i)
    b = perm(M, i)
    c = pow(perm(M - i, N - i), 2, MOD)
    cnt = (a * b * c) % MOD
    ans = (ans + flag * cnt) % MOD
    flag *= -1
print(ans)
