#こんなんでいいのかな
import sys
def 解():
    iN,iM = [int(_) for _ in input().split()]
    aData = [[int(_) for _ in sLine.split()] for sLine in sys.stdin.readlines()]
    def addPath(d,a,b):
        if a in d:
            d[a].add(b)
        else:
            d[a]={b}
    dT = {}
    for a,b in aData:
        addPath(dT,a,b)
        addPath(dT,b,a)

    def dfs(dT,iStart,iC):
        if len(dsVisited) == iN:
            iC += 1
            return iC
        for i in dT[iStart] - dsVisited:
            dsVisited.add(i)
            iC = dfs(dT,i,iC)
            dsVisited.remove(i)
        return iC

    dsVisited = {1}
    print(dfs(dT,1,0))
解()
