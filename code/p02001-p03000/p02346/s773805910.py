# Range Sum Query (RSQ)
D = [0]
[n, q] = list(map(int, input().split()))

def initRMQ(n_):
    global D, n
    size = 1
    while size < n_:
        size *= 2
    i = 1
    while i <= 2*size - 1 - 1:
        D.append(0)
        i += 1
    n = size

def add(k, a):
    global D
    k += n - 1
    D[k] += a
    while k > 0:
        k = int((k - 1)/2)
        D[k] = D[k*2 + 1] + D[k*2 + 2]

def query(a, b, k, l, r):
    global D
    if r <= a or b <= l:
        return 0
    if a <= l and r <= b:
        return D[k]

    vl = query(a, b, k*2 + 1, l, int((l + r)/2))
    vr = query(a, b, k*2 + 2, int((l + r)/2), r)
    return vl + vr

def getSum(a, b):
    global n
    return query(a, b + 1, 0, 0, n)

initRMQ(n)
for i in range(q):
    data = list(map(int, input().split()))
    if data[0] == 0:
        add(data[1] - 1, data[2])
    if data[0] == 1:
        print(getSum(data[1] - 1, data[2] - 1))
