def solve():
    N = int(input())
    Hs = list(map(int, input().split()))
    As = list(map(int, input().split()))

    def makeBIT(numEle):
        numPow2 = 2 ** (numEle-1).bit_length()
        data = [0] * (numPow2+1)
        return data, numPow2
    def setValue(iA, A):
        iB = iA + 1
        while iB <= numPow2:
            if A > data[iB]:
                data[iB] = A
            iB += iB & -iB
    def getMax(iA):
        iB = iA + 1
        ans = 0
        while iB > 0:
            if data[iB] > ans:
                ans = data[iB]
            iB -= iB & -iB
        return ans


    iHs = list(range(N))
    iHs.sort(key=lambda iH: Hs[iH])
    odrHs = [0]*(N)
    for odrH, iH in enumerate(iHs):
        odrHs[iH] = odrH

    data, numPow2 = makeBIT(N)

    ans = 0
    for odrH in range(N):
        iH = iHs[odrH]
        v = As[iH] + getMax(iH)
        if v > ans:
            ans = v
        setValue(iH, v)

    print(ans)


solve()
