from collections import Counter
from itertools import product

def solve():
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

    def getPrimeFactors(x, minPFs):
        anss = []
        while minPFs[x] > 1:
            anss.append(minPFs[x])
            x //= minPFs[x]
        return anss

    maxA = max(As)
    minPFs = getMinPFs(maxA)
    As.sort()

    cntA = Counter(As)

    ans = 0
    setA = set()
    for A in As:
        if cntA[A] == 1:
            PFs = getPrimeFactors(A, minPFs)
            cnt = Counter(PFs)
            ps = list(cnt.keys())
            es = [range(cnt[p]+1) for p in ps]
            L = len(ps)
            for nums in product(*es):
                d = 1
                for i in range(L):
                    d *= ps[i]**nums[i]
                if d in setA:
                    break
            else:
                ans += 1

        setA.add(A)

    print(ans)


solve()
