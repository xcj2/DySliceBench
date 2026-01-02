import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def solve():
    MOD = 998244353

    def makeBIT(numEle):
        numPow2 = 2 ** (numEle-1).bit_length()
        data = [0] * (numPow2+1)
        return data, numPow2
    def setInit(As):
        for iB, A in enumerate(As, 1):
            data[iB] = A
        for iB in range(1, numPow2):
            i = iB + (iB & -iB)
            data[i] += data[iB]
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
    def getRangeSum(iFr, iTo):
        return getSum(iTo) - getSum(iFr-1)


    N, K = map(int, input().split())
    LRs = [tuple(map(int, input().split())) for _ in range(K)]

    data, numPow2 = makeBIT(N)

    addValue(0, 1)

    for i in range(1, N):
        v = 0
        for L, R in LRs:
            x, y = i-R, i-L
            if y < 0:
                continue
            if x < 0:
                x = 0
            v += getRangeSum(x, y) % MOD
            v %= MOD
        addValue(i, v)

    ans = getRangeSum(N-1, N-1) % MOD
    print(ans)


solve()
