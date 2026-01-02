# Range Minimum Query (RMQ)
INF = 2**31 - 1
D = [INF]
[n, q] = list(map(int, input().split()))

def initRMQ(n_):
    global D, n
    size = 1
    while size < n_:
        size *= 2
    i = 1
    while i <= 2*size - 1 - 1:
        D.append(INF)
        i += 1
    n = size

def update(k, a):
    global n
    k += n - 1
    D[k] = a
    while k > 0:
        k = int((k - 1)/2)
        D[k] = min(D[k*2 + 1], D[k*2 + 2])

def query(a, b, k, l, r):
    global INF, D
    if r <= a or b <= l:
        return INF
    if a <= l and r <= b:
        return D[k]

    vl = query(a, b, k*2 + 1, l, int((l + r)/2))
    vr = query(a, b, k*2 + 2, int((l + r)/2), r)
    return min(vl, vr)

def findMin(a, b):
    global n
    return query(a, b + 1, 0, 0, n)

initRMQ(n)

for i in range(q):
    data = list(map(int, input().split()))
    if data[0] == 0:
        update(data[1], data[2])
    if data[0] == 1:
        print(findMin(data[1], data[2]))




