from collections import Counter

def solve():
    MOD = 10**9 + 7
    maxA = 10**6

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

    N = int(input())
    As = list(map(int, input().split()))

    cntP = Counter()
    for A in As:
        PFs = getPrimeFactors(A)
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
