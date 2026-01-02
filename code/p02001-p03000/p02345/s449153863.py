import sys
sys.setrecursionlimit(10000)

INF = 2147483647


# initiate the RMQ tree
def initRMQ(n, D):
    n_ = 1
    # search the power of n
    while n_ < n:
        n_ *= 2
    # set a big number to all leaves
    for i in range(2*n_ - 1):
        D.append(INF)

    return n_


def update(k, a):
    k += n_ - 1  # convert array index to tree index
    D[k] = a
    while k != 0:
        k = int((k - 1) / 2)
        D[k] = min(D[k*2 + 1], D[k*2 + 2])


def findMin(qlow, qhigh):
    return query(qlow, qhigh + 1, 0, 0, n_)


def query(qlow, qhigh, k, l, r):
    # print('q', a, b, k, l, r)
    if r <= qlow or qhigh <= l:
        return INF

    if qlow <= l and r <= qhigh:
        return D[k]

    mid = (l + r) // 2
    vl = query(qlow, qhigh, k*2 + 1, l, mid)
    vr = query(qlow, qhigh, k*2 + 2, mid, r)

    return min(vl, vr)


if __name__ == '__main__':
    n, q = map(int, input().split())

    D = []
    n_ = initRMQ(n, D)

    for _ in range(q):
        # print(D)
        c, x, y = map(int, input().split())

        if c == 0:
            update(x, y)

        else:
            print(findMin(x, y))

