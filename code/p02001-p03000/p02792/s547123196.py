#グローバル変数
ab = []
def solve0(n):
    ok = 0
    for a in range(1,n+1):
        for b in range(1,n+1):
            if str(a)[0] == str(b)[-1] and str(a)[-1] == str(b)[0]:
                ok += 1
                ab.append([a,b])
    return ok

def solve2(n,ab):
    ok = 0
    ok_a = 0
    ok_b = 0
    for a,b in ab:
        ok_a = count(n,a)
        ok_b = count(n,b)
        ok = ok + ok_a * ok_b
    return ok

def count(n,z):
    strN = str(n)
    strZ = str(z)
    if z > n:       # z の方が大きい場合は 0
        return 0
    if len(strN) == 1: #　n　の桁が１桁の場合
        return 1
    if len(strZ) == 1: #　z　の桁が１桁の場合
        return 1

    #　n と z　の桁が2桁以上の場合
    ok = 0
    mlen = 0
    while mlen+2 < len(strN): # z の桁が n より小さい
        ok = ok + 10**mlen
        mlen = mlen + 1
    # n と z　の桁が同じ
    if int(strZ[0]+"9"*mlen+strZ[-1]) <= n:
        ok = ok + 10**mlen
    elif int(strZ[0]+strN[1:len(strN)-1]+strZ[-1]) <= n:
        ok = ok + int(strN[1:len(strN)-1])+1
    else:
        nMid = str(strN[1:len(strN)-1])
        if int(nMid) > 0:
            nMid = str(int(nMid)-1).zfill(len(strN)-2)
            if int(strZ[0]+nMid+strZ[-1]) <= n:
                ok = ok + (int(nMid))+1
    return ok

# 配列 ab の準備
solve0(99)

# 整数の入力
n = int(input())
print(solve2(n,ab))
