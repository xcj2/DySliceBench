def 解法3優先度付きキュー():
    import heapq
    X,Y,Z,K = [int(_) for _ in input().split()]
    aA = sorted((int(_) for _ in input().split()),reverse=True)
    aB = sorted((int(_) for _ in input().split()),reverse=True)
    aC = sorted((int(_) for _ in input().split()),reverse=True)
    dS=set()
    aAns = [0]*K
    aQ = []
    def fPush(aQ,i,j,k):
        if X <= i :
            i = X-1
        if Y <= j:
            j = Y-1
        if Z <= k:
            k = Z-1
        if (i,j,k) not in dS:
            heapq.heappush(aQ,(-1*(aA[i]+aB[j]+aC[k]),i,j,k))
            dS.add((i,j,k))
    def fPop(aQ):
        iD,i,j,k = heapq.heappop(aQ)
        return (-1*iD,i,j,k)
    fPush(aQ,0,0,0)
    for iU in range(K):
        aAns[iU],i,j,k = fPop(aQ)
        fPush(aQ,i+1,j,k)
        fPush(aQ,i,j+1,k)
        fPush(aQ,i,j,k+1)

    print(*aAns,sep="\n")

解法3優先度付きキュー()
