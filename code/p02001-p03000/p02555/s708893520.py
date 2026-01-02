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


S = int(input())
modFacts, invs = prepare(10 * S)
ans = 0
for k in range(1, S // 3 + 1):
    s = S - 3 * k
    cnt = comb(k - 1 + s, s)
    ans += cnt
    ans %= MOD
print(ans)
