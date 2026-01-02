import sys
input = sys.stdin.readline

def solve():
    INF = float('inf')
    idEle = -INF
    def _binOpe(x, y):
        return x if x >= y else y
    def makeSegTreeLazy(numEle):
        numPow2 = 2 ** (numEle-1).bit_length()
        data = [idEle] * (2*numPow2)
        lazy = [0] * (2*numPow2)
        return data, lazy, numPow2
    def setInit(As):
        for iST, A in enumerate(As, numPow2):
            data[iST] = A
        for iST in reversed(range(1, numPow2)):
            data[iST] = _binOpe(data[2*iST], data[2*iST+1])
    def _update1(iST, A):
        vIfSet = _getVIfSet(iST, A)
        data[iST] += vIfSet
        lazy[iST] += A
    def _getVIfSet(iST, A):
        return A
    def _getIndices(iSt, iEn):
        iSTs = []
        L = iSt + numPow2
        R = iEn + numPow2
        L0 = L // (L & -L)
        R0 = R // (R & -R)
        while L < R:
            if L < L0:
                iSTs.append(L)
            if R < R0:
                iSTs.append(R)
            L >>= 1
            R >>= 1
        while L:
            iSTs.append(L)
            L >>= 1
        return iSTs
    def _propagate(iST):
        v = lazy[iST]
        if v:
            _update1(2*iST, v)
            _update1(2*iST+1, v)
            lazy[iST] = 0
    def update(iSt, iEn, A):
        iSTs = _getIndices(iSt, iEn)
        for iST in reversed(iSTs):
            _propagate(iST)
        L = iSt + numPow2
        R = iEn + numPow2
        while L < R:
            if L & 1:
                _update1(L, A)
                L += 1
            if R & 1:
                R -= 1
                _update1(R, A)
            L >>= 1
            R >>= 1
        for iST in iSTs:
            data[iST] = _binOpe(data[2*iST], data[2*iST+1])
    def getValue(iSt, iEn):
        iSTs = _getIndices(iSt, iEn)
        for iST in reversed(iSTs):
            _propagate(iST)
        ans = idEle
        L = iSt + numPow2
        R = iEn + numPow2
        while L < R:
            if L & 1:
                ans = _binOpe(ans, data[L])
                L += 1
            if R & 1:
                R -= 1
                ans = _binOpe(ans, data[R])
            L >>= 1
            R >>= 1
        return ans


    N, M = map(int, input().split())
    LRs = [[] for _ in range(N+1)]
    for _ in range(M):
        L, R, A = map(int, input().split())
        LRs[R].append((L, A))

    data, lazy, numPow2 = makeSegTreeLazy(N+1)
    setInit([0]*(N+1))

    for R in range(1, N+1):
        v = getValue(0, R)
        v0 = getValue(R, R+1)
        update(R, R+1, v-v0)
        for L, A in LRs[R]:
            update(L, R+1, A)

    ans = getValue(0, N+1)
    print(ans)


solve()
