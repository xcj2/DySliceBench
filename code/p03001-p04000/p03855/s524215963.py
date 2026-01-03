#Union-Find木の構築
import sys
def 解():
    iN,iK,iL = [int(_) for _ in input().split()]
    aD = [[int(_) for _ in sLine.split()] for sLine in sys.stdin.readlines()]

    def buildTree(a):
        #aT = [0]*(iN+1)
        aT = list(range(iN+1))
        for p,q in a:
            rp = getRoot(aT,p)
            rq = getRoot(aT,q)
            thisRoot = max(rp,rq,q) #みんな小さい方に合わせてるのでデカい方に合>わせてみる
            aT[p] = thisRoot
            aT[q] = thisRoot
            aT[rp] = thisRoot #これで Union してるつもり
            aT[rq] = thisRoot
        return aT
    def getRoot(a,i): #find
        #if a[i] == i or a[i] == 0:
        #   if a[i] == 0 : a[i] = i
        if a[i] == i :
            return i
    #   elif i < a[i] :
        else :
            a[i] = getRoot(a,a[i])
            return a[i]
    #   else:
    #       print("! ",i,a[i])

    aT道 = buildTree(aD[0:iK])
    aT鉄道 = buildTree(aD[iK:])
    aRet = []
    dRet = {}
    for i in range(1,iN+1):
        # いやはやこんなもんもキーになるのか。
        Comb = (getRoot(aT道,i), getRoot(aT鉄道,i))
        aRet.append(Comb)
        if Comb in dRet:
            dRet[Comb] += 1
        else:
            dRet[Comb] = 1
    print(" ".join([str(dRet[_]) for _ in aRet]))

解()
