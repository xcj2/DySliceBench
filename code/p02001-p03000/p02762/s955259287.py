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
    N,M,K = map(int, input().split())

    ds = [i for i in range(N+1)]
    cntOfF = [0]*(N+1)
    blocks = [set() for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        dsUnion(ds, a, b)
        cntOfF[a] += 1 
        cntOfF[b] += 1 

    for _ in range(K):
        c, d = map(int, input().split())
        blocks[c].add(d)
        blocks[d].add(c)

    Q = {}
    for i in range(1, N+1):
        root = dsFind(ds, i)
        if not(root in Q):
            Q[root] = set()

        Q[root].add(i)
    
    X = []
    for i in range(1, N+1):
        root = dsFind(ds, i)
        q = Q[root]
        block = blocks[i]

        x = len(q) - 1 - cntOfF[i] - len(q&block)
        X.append(x)

    print(' '.join(map(str, X)))



main()
