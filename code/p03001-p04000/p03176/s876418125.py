def init(init_val):
    for i in range(n):
        MI[i+num-1] = init_val[i]
        MA[i+num-1] = init_val[i]
    for i in range(num-2, -1, -1):
        MI[i] = min(MI[2*i+1], MI[2*i+2])
        MA[i] = max(MA[2*i+1], MA[2*i+2])


def update(k, x):
    k += num-1
    MI[k] = x
    MA[k] = x
    while k+1:
        k = (k-1)//2
        MI[k] = min(MI[k*2+1], MI[k*2+2])
        MA[k] = max(MA[k*2+1], MA[k*2+2])


def rangemin(p, q):
    if q <= p:
        return 1 << 100
    p += num-1
    q += num-2
    res = 1 << 100
    while q-p > 1:
        if p & 1 == 0:
            res = min(res, MI[p])
        if q & 1 == 1:
            res = min(res, MI[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = min(res, MI[p])
    else:
        res = min(min(res, MI[p]), MI[q])
    return res


def rangemax(p, q):
    if q <= p:
        return -1
    p += num-1
    q += num-2
    res = -1
    while q-p > 1:
        if p & 1 == 0:
            res = max(res, MA[p])
        if q & 1 == 1:
            res = max(res, MA[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = max(res, MA[p])
    else:
        res = max(max(res, MA[p]), MA[q])
    return res


n = int(input())
h = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

dp = [0 for _ in range(n+1)]

num = 2**(n).bit_length()
MI = [1 << 100]*2*num
MA = [-1]*2*num
init(dp)

for i in range(n):
    update(h[i], a[i] + rangemax(0, h[i]))

print(rangemax(0, n+1))
