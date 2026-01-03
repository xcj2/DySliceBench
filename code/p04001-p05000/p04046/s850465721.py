iH,iW,iA,iB = [int(x) for x in input().split()]
iD = 10**9+7 #法

#初等整数論勉強して解説通りキッチリ実装したった

#二分累乗法 iDを法として
def fBiPow(iX,iN,iD):
    iY = 1
    while iN > 0:
        if iN % 2 == 0:
            iX = iX * iX % iD
            iN = iN // 2
        else:
            iY = iX * iY % iD
            iN = iN - 1
    return iY

#nCr = n!/r!(n-r)!
#ループ回すだけ版や
def fFr(iX,iR=1):
    if iR == 0 or iX == 0:
        return 1
    else :
        iRet = 1
        for i in range(iR,iX+1):
            iRet *= i
        return iRet

def fnCr(iN,iR):
    if iR == 0:
        return 1
    else:
        return fFr(iN,iR+1) // fFr(iN-iR)

#階乗(iDを法とした)の配列
aM = [1]*(iH+iW-1)
for i in range(1,iH+iW-1):
    aM[i]=aM[i-1]*i %iD
#各階乗のiDを法とした逆元の配列
aInvM = [1]*(iH+iW-1)
aInvM[iH+iW-2] = fBiPow(aM[iH+iW-2],iD-2,iD)
for i in range(iH+iW-2,0,-1):
    aInvM[i-1]=aInvM[i]*i % iD

iRet = 0
for iL in range(0,iH-iA):
    #iRet += (fnCr(iL+iB-1,iL) * fnCr(iW-iB+iH-iL-2,iW-iB-1))%iD
    iRet += (aM[iL+iB-1]*aInvM[iL]*aInvM[iB-1]) % iD * (aM[iW-iB+iH-iL-2]*aInvM[iW-iB-1]*aInvM[iH-iL-1])%iD
    iRet %= iD
iRet %= iD
print(iRet)
