from itertools import combinations

def solve():
    INF = 10**5

    def getNumInversion(odrAs):
        def makeBIT(numEle):
            numPow2 = 2 ** (numEle-1).bit_length()
            data = [0] * (numPow2+1)
            return data, numPow2
        def addValue(iA, A):
            iB = iA + 1
            while iB <= numPow2:
                data[iB] += A
                iB += iB & -iB
        def getSum(iA):
            iB = iA + 1
            ans = 0
            while iB > 0:
                ans += data[iB]
                iB -= iB & -iB
            return ans
        lenA = len(odrAs)
        data, numPow2 = makeBIT(lenA)
        ans = 0
        for odrA in reversed(odrAs):
            ans += getSum(odrA)
            addValue(odrA, 1)
        return ans

    N = int(input())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))

    ans = INF
    for iEvens in combinations(range(N), r=N//2):
        iEvens = set(iEvens)
        COdds, CEvens = [], []
        for i in range(N):
            if i in iEvens:
                if i % 2:
                    CEvens.append((As[i], i))
                else:
                    CEvens.append((Bs[i], i))
            else:
                if i % 2:
                    COdds.append((Bs[i], i))
                else:
                    COdds.append((As[i], i))
        COdds.sort()
        CEvens.sort()

        Cs = []
        for COdd, CEven in zip(COdds, CEvens):
            Cs += [COdd, CEven]
        if N % 2:
            Cs += [COdds[-1]]

        for i in range(N-1):
            if Cs[i][0] > Cs[i+1][0]:
                break
        else:
            odrAs = [i for C, i in Cs]
            num = getNumInversion(odrAs)
            ans = min(ans, num)
            if ans == 0:
                break

    if ans == INF:
        print(-1)
    else:
        print(ans)


solve()
