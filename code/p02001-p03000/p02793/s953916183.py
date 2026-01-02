from collections import Counter

def solve():
    MOD = 10**9 + 7
    maxA = 10**6

    N = int(input())
    As = list(map(int, input().split()))

    def getMinPFs(n):
        isPrimes = [False]*2 + [True]*(n-1)
        minPFs = [1] + list(range(1, n+1))
        for d in range(2, int(n**0.5)+1):
            if isPrimes[d]:
                minPFs[d] = d
                for x in range(d*d, n+1, d):
                    isPrimes[x] = False
                    if minPFs[x] == x:
                        minPFs[x] = d
        return minPFs

    minPFs = getMinPFs(maxA)

    def getPrimeFactors(x, minPFs):
        anss = []
        while minPFs[x] > 1:
            anss.append(minPFs[x])
            x //= minPFs[x]
        return anss

    cntP = Counter()
    for A in As:
        PFs = getPrimeFactors(A, minPFs)
        for key, num in Counter(PFs).items():
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

    invs = getInvs(maxA, MOD)

    ans = 0
    for A in As:
        ans += lcmA * invs[A]
        ans %= MOD

    print(ans)

solve()
