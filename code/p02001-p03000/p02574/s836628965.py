from functools import reduce
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def solve():
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

    def getPrimeFactors(x, minPFs):
        anss = set()
        while minPFs[x] > 1:
            anss.add(minPFs[x])
            x //= minPFs[x]
        return anss

    minPFs = getMinPFs(maxA)

    useds = [0] * (maxA+1)
    for A in As:
        PFs = getPrimeFactors(A, minPFs)
        for PF in PFs:
            if useds[PF]:
                break
            useds[PF] = 1
        else:
            continue
        break
    else:
        print('pairwise coprime')
        return

    def gcd(a, b):
        while b:
            a, b = b, a%b
        return a

    g = reduce(gcd, As)

    if g == 1:
        print('setwise coprime')
    else:
        print('not coprime')


solve()
