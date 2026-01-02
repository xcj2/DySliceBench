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



def dsUpdate(ds):
    for x0 in ds:
        x = x0
        while ds[x] != x:
            x = ds[x]

        root = x
        x = x0

        while ds[x] != root:
            y = ds[x]
            ds[x] = root
            x = y


def main():
    N, M = map(int, input().split())
    P = list(map(int, input().split()))

    ds = {x:x for x in range(1, N+1)}
    for x, y in [map(int, input().split()) for _ in range(M)]:
        dsUnion(ds, x, y)
        
    dsUpdate(ds)

    Q = {}
    for x, root in ds.items():
        if not root in Q:
            Q[root] = set()

        Q[root].add(x)

    cnt = 0

    for q in Q.values():
        p = set(P[x-1] for x in q)
        cnt += len(q&p)

    print(cnt)



if __name__ == '__main__':
    main()
