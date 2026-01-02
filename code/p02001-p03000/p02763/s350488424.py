def solve():
    import sys
    input = sys.stdin.readline

    numChar = 26
    #numChar = 5
    ordA = ord('a')

    N = int(input())
    Ss = input()
    nos = [ord(S)-ordA for S in Ss]
    Q = int(input())

    def makeBIT(numEle):
        numPow2 = 2 ** (numEle-1).bit_length()
        datas = [[0]*(numPow2+1) for _ in range(numChar)]
        return datas, numPow2
    def addValue(no, iA, A):
        data = datas[no]
        iB = iA + 1
        while iB <= numPow2:
            data[iB] += A
            iB += iB & -iB
    def getSum(no, iA):
        data = datas[no]
        iB = iA + 1
        ans = 0
        while iB > 0:
            ans += data[iB]
            iB -= iB & -iB
        return ans
    def getRangeSum(no, iFr, iTo):
        return getSum(no, iTo) - getSum(no, iFr-1)


    datas, numPow2 = makeBIT(N)

    for i in range(N):
        no = nos[i]
        addValue(no, i, 1)

    anss = []
    for _ in range(Q):
        tp, v1, v2 = input().split()
        if tp == '1':
            pos = int(v1)-1
            no1 = nos[pos]
            no2 = ord(v2)-ordA
            addValue(no1, pos, -1)
            addValue(no2, pos, 1)
            nos[pos] = no2
        else:
            L, R = int(v1)-1, int(v2)-1
            ans = 0
            for no in range(numChar):
                if getRangeSum(no, L, R):
                    ans += 1
            anss.append(ans)

    print('\n'.join(map(str, anss)))


solve()
