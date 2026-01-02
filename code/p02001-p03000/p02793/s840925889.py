from collections import Counter

def solve():
    MOD = 10**9 + 7

    N = int(input())
    As = list(map(int, input().split()))

    def getPrimeFactors(x):
        anss = []
        while x%2 == 0:
            anss.append(2)
            x //= 2
        for d in range(3, int(x**0.5)+1, 2):
            while x%d == 0:
                anss.append(d)
                x //= d
        if x != 1:
            anss.append(x)
        return anss

    maxCnt = Counter()
    for A in As:
        PFs = getPrimeFactors(A)
        cnt = Counter(PFs)
        maxCnt |= cnt

    LCM = 1
    for p, e in maxCnt.items():
        LCM *= pow(p, e, MOD)
        LCM %= MOD

    maxA = max(As)

    def getInvs(n, MOD):
        invs = [1] * (n+1)
        for x in range(2, n+1):
            invs[x] = (-(MOD//x) * invs[MOD%x]) % MOD
        return invs
    invs = getInvs(maxA, MOD)

    sumInv = 0
    for A in As:
        sumInv += invs[A]
        sumInv %= MOD

    ans = LCM * sumInv % MOD
    print(ans)


solve()
