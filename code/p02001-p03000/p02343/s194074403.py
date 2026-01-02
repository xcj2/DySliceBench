
def union(x, y):
    link(findSet(x), findSet(y))

def link(x, y):
    if r[x] > r[y]:
        p[y] = x
    else:
        p[x] = y
        if r[x] == r[y]: r[y] = r[y] + 1

def findSet(x):
    if x != p[x]:
        p[x] = findSet(p[x])
    return p[x]


if __name__ == '__main__':

    p = [];
    r = [];

    n_set, n_quare = map(int, input().split())

    for i in range(n_set):
        p.append(i)
        r.append(0)


    for i in range(n_quare):
        q, x, y = map(int, input().split())

        if q == 0:
            union(x, y)

        else:
            print(int(findSet(x) == findSet(y)))

