
#偶奇合わせてたのはグルグル回してたからだが
#一意に決めるんなら偶奇合わせる必要ないのでは
def 解():
    N = int(input())
    dA ={}
    def lenbin(a):
        return len(bin(a)) - 2
    def addData(oDict,a):
        if a in oDict:
            oDict[a]+=1
        else:
            oDict[a]=1
    for a in map(int,input().split()):
        addData(dA,a)
    def searchPair(oD):
        iC = 0
        for a in sorted(oD.keys(),reverse=True):
            if oD[a]:
                t = ( 1 << lenbin(a)) - a
                if t == a:
                    iAT = oD[a] // 2
                    iC += iAT
                    oD[a] -= iAT *2
                elif t in oD:
                    iAT = min(oD[a],oD[t])
                    iC += iAT
                    oD[a] -= iAT
                    oD[t] -= iAT
        return iC
    print(searchPair(dA))
解()
