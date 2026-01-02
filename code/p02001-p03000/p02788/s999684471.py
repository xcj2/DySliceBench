def solve():
    from bisect import bisect_left, bisect_right
    import sys
    input = sys.stdin.readline

    def makeBIT(numEle):
        numPow2 = 2 ** (numEle-1).bit_length()
        data = [0] * (numPow2+1)
        return data, numPow2
    def setInit(As):
        for iB, A in enumerate(As, 1):
            data[iB] = A
        for iB in range(1, numPow2):
            i = iB + (iB & -iB)
            data[iB] -= data[i]
    def addValue(iA, A):
        iB = iA + 1
        while iB > 0:
            data[iB] += A
            iB -= iB & -iB
    def getValue(iA):
        iB = iA + 1
        ans = 0
        while iB <= numPow2:
            ans += data[iB]
            iB += iB & -iB
        return ans
    def addRangeValue(iFr, iTo, A):
        addValue(iTo, A)
        if iFr > 0:
            addValue(iFr-1, -A)

    N, D, A = map(int, input().split())
    XHs = [tuple(map(int, input().split())) for _ in range(N)]

    XHs.sort()
    Xs = [X for X, H in XHs]
    Hs = [H for X, H in XHs]

    data, numPow2 = makeBIT(N)
    setInit(Hs)

    ans = 0
    for iL in range(N):
        H = getValue(iL)
        if H <= 0: continue
        iR = bisect_right(Xs, Xs[iL]+2*D) - 1
        num = -(-H // A)
        addRangeValue(iL, iR, -num*A)
        ans += num

    print(ans)


solve()
