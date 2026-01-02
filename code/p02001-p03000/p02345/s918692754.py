INF = 10 ** 20

n, q = map(int, input().split())
n_t = 1
seg_tree = []


def initRMQ(n):
    global n_t
    while n_t < n:
        n_t *= 2
    for i in range(0, 2*n_t - 1):
        seg_tree.append(2 ** 31 - 1)


def update(k, x):
    k += n_t - 1
    seg_tree[k] = x
    while k > 0:
        k = (k - 1) // 2
        seg_tree[k] = min(seg_tree[k * 2 + 1], seg_tree[k * 2 + 2])


def findMin(a, b):
    return query(a, b+1, 0, 0, n_t)


def query(a, b, k, l, r):
    if r <= a or b <= l:
        return INF
    if a <= l and r <= b:
        return seg_tree[k]
    else:
        vl = query(a, b, k*2 + 1, l, (l + r) // 2)
        vr = query(a, b, k*2 + 2, (l + r) // 2, r)
        return min(vl, vr)


initRMQ(n)
for _ in range(q):
    com, x, y = map(int, input().split())
    if not com:
        update(x, y)
    else:
        print(findMin(x, y))
