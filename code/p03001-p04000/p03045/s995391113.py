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
    N, M = map(int, input().split())
    ds = {}

    for i in range(N):
        dsMakeSet(ds, i+1)

    n = 0
    for i in range(M):
        X,Y,Z = map(int, input().split())
        if dsUnion(ds, X, Y):
            n += 1
        
    print(N - n)
        

if __name__ == '__main__':
    main()
