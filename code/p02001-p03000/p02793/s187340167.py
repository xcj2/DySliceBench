from collections import Counter

def solve():
    MOD = 10**9 + 7
    maxA = 10**6

    N = int(input())
    As = list(map(int, input().split()))

    isPrimes = [False]*2 + [True]*(maxA-1)
    minFs = [1] * (maxA+1)
    for i in range(2, int(maxA**0.5) + 1):
        if isPrimes[i]:
            for x in range(i*i, maxA+1, i):
                isPrimes[x] = False
                minFs[x] = i

    def getPrimeFactors(x):
        anss = []
        while minFs[x] > 1:
            anss.append(minFs[x])
            x //= minFs[x]
        if x != 1:
            anss.append(x)
        return anss

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
