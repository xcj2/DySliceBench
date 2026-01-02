def prov(maskHor, maskVert):
    kol = 0
    for i in range(h):
        for j in range(v):
            if m[i][j] == '#':
                b = 0
                for hor in maskHor:
                    if hor == i:
                        b = 1
                for vert in maskVert:
                    if vert == j:
                        b = 1
                if b == 0:
                    kol += 1
    #tmh = maskHor
    #for i in range(len(tmh)):
    #    tmh[i] = str(tmh[i])
    #tmv = maskVert
    #for i in range(len(tmv)):
    #    tmv[i] = str(tmv[i])
    #print('!', ' '.join(tmh), '!', ' '.join(tmv), '!', kol)
    if kol == k:
        global ans
        ans += 1


def genMaskVert(pos, mask, maskHor):
    if (pos == v):
        prov(maskHor, mask)
        #if not len(mask) == 0:
        #    mask.pop()
        return
    else:
        genMaskVert(pos + 1, mask, maskHor)
        temp = mask
        temp.append(pos)
        genMaskVert(pos + 1, temp, maskHor)
        if not len(mask) == 0:
            mask.pop()
        return


def genMaskHor(pos, mask):
    if (pos == h):
        genMaskVert(0, [], mask)
        #if not len(mask) == 0:
        #    mask.pop()
        return
    else:
        genMaskHor(pos + 1, mask)
        mask.append(pos)
        genMaskHor(pos + 1, mask)
        if not len(mask) == 0:
            mask.pop()
        return


h, v, k = input().split()
h = int(h)
v = int(v)
k = int(k)
ans = 0
m = []
for i in range(h):
    m.append(input())
genMaskHor(0, [])
print(ans)
