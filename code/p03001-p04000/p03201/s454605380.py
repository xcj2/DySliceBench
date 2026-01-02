N = int(input())
dA1 ={}
dA0 ={}
def lenbin(a):
    return len(bin(a)) - 2
def addData(oDict,a):
    if a in oDict:
        oDict[a]+=1
    else:
        oDict[a]=1
for a in input().split():
    a = int(a)
    if a % 2 :
        addData(dA1,a)
    else:
        addData(dA0,a)
def searchPair(oD):
    iC = 0
    for a in sorted(oD.keys(),reverse=True):
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
#iC = 0
#iC += searchPair(dA1)
#iC += searchPair(dA0)
print(searchPair(dA1)+searchPair(dA0))

