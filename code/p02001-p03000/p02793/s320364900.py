from collections import Counter

def solve():
    MOD = 10**9 + 7

    def getPrimeFactors(x):
        anss = []
        for d in range(2, int(x**0.5)+1):
            while x%d == 0:
                anss.append(d)
                x //= d
        if x != 1:
            anss.append(x)
        return anss

    N = int(input())
    As = list(map(int, input().split()))

    PFss = []
    Primes = set()
    for A in As:
        PFs = getPrimeFactors(A)
        cnt = Counter(PFs)
        PFss.append(cnt)
        Primes |= cnt.keys()

    cntP = Counter()
    for PFs in PFss:
        for key, num in PFs.items():
            cntP[key] = max(cntP[key], num)

    lcmA = 1
    for key, num in cntP.items():
        lcmA *= pow(key, num, MOD)
        lcmA %= MOD

    def getInvs(n, MOD):
        invs = [1] * (n+1)
        for x in range(2, n+1):
            invs[x] = (-(MOD//x) * invs[MOD%x]) % MOD
        return invs

    invs = getInvs(10**6, MOD)

    ans = 0
    for A in As:
        ans += lcmA * invs[A]
        ans %= MOD

    print(ans)

solve()
