n = int(input())

zyunnsitigoL = [3, 5, 7]

def zyunnsitigo(zyunsiL):
    index=0
    newSitiL=[]
    while index < len(zyunsiL):
        newSitiL.append(int(str(zyunsiL[index])+"3"))
        newSitiL.append(int(str(zyunsiL[index])+"5"))
        newSitiL.append(int(str(zyunsiL[index])+"7"))
        index+=1
    return newSitiL

def sitigoCounter(n, zyunsiL):
    index =0
    count =0
    while index < len(zyunsiL):
        if zyunsiL[index]<n+1:
            newSL = list(map(int, list(str(zyunsiL[index]))))
            if 3 in newSL and 5 in newSL and 7 in newSL:
                if 0 in newSL or 1 in newSL or 2 in newSL or 4 in newSL or 6 in newSL or 8 in newSL or 9 in newSL:
                    pass
                else:
                    count+=1
        index+=1
    return count

def listMaker(n, zyunsiL):
    if n < 10:
        return zyunsiL
    else:
        newL = zyunnsitigo(zyunsiL)
        zyunsiL.extend(newL)
        if n > 100:
            newL=zyunnsitigo(newL)
            zyunsiL.extend(newL)
            if n > 1000:
                newL = zyunnsitigo(newL)
                zyunsiL.extend(newL)
                if n > 10000:
                    newL = zyunnsitigo(newL)
                    zyunsiL.extend(newL)
                    if n > 100000:
                        newL = zyunnsitigo(newL)
                        zyunsiL.extend(newL)
                        if n > 1000000:
                            newL = zyunnsitigo(newL)
                            zyunsiL.extend(newL)
                            if n > 10000000:
                                newL = zyunnsitigo(newL)
                                zyunsiL.extend(newL)
                                if n > 100000000:
                                    newL = zyunnsitigo(newL)
                                    zyunsiL.extend(newL)
        return zyunsiL

zyunsiL = listMaker(n, zyunnsitigoL)
ans = sitigoCounter(n, zyunsiL)
print(ans)