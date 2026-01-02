from itertools import accumulate

N = int(input())
As = list(map(int, input().split()))

Bs = sorted(As)
M = N*(N+1)//2

def isOK(mid):
    Am = Bs[mid]
    Ss = [1 if A >= Am else -1 for A in As]
    Ss = list(accumulate([0]+Ss))

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

    data, numPow2 = makeBIT(N+1)
    iSs = list(range(N+1))
    iSs.sort(key=lambda iS: Ss[iS])
    odrSs = [0]*(N+1)
    for odrS, iS in enumerate(iSs):
        odrSs[iS] = odrS

    num = 0
    for odrS in odrSs:
        num += getSum(odrS)
        addValue(odrS, 1)
    return num >= (M+1)//2


ng, ok = N, -1
while abs(ok-ng) > 1:
    mid = (ng+ok) // 2
    if isOK(mid):
        ok = mid
    else:
        ng = mid

print(Bs[ok])
