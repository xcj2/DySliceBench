#  --*-coding:utf-8-*--


def dsMakeSet(ds, x):
    ds[x] = x


def dsFind(ds, x):
    if ds[x] == x:
        return x

    x0 = x
    while ds[x] != x:
        x = ds[x]

    ds[x0] = x
    return x


def dsUnion(ds, x, y):
    xRoot = dsFind(ds, x)
    yRoot = dsFind(ds, y)
    
    if xRoot != yRoot:
        ds[yRoot] = xRoot
        return True

    return False



def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    ds = {}
    for i in range(H):
        s0 = S[i-1] if i > 0 else None
        s1 = S[i]

        for j in range(W):
            dsMakeSet(ds, (i, j))

            if j > 0 and s1[j-1] != s1[j]:
                dsUnion(ds, (i, j-1), (i, j))
                
            if i > 0 and s0[j] != s1[j]:
                dsUnion(ds, (i-1, j), (i, j))
            
    bCnt = {}
    wCnt = {}

    for x in ds:
        y = dsFind(ds, x)
        
        if not y in bCnt:
            bCnt[y] = 0
            wCnt[y] = 0

        if S[x[0]][x[1]] == '#':
            bCnt[y] += 1
        else:
            wCnt[y] += 1

    s = sum(bCnt[x]*wCnt[x] for x in bCnt)
    print(s)
                

    


if __name__ == '__main__':
    main()
