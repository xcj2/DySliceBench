dat = [None] * 400000
m = 0

def init():
    global dat, m
    for i in range(2 * m - 1):
        dat[i] = 2 ** 31 - 1

def update(i, x):
    global dat, m
    i += m - 1
    dat[i] = x
    while i > 0:
        i = (i - 1) // 2
        dat[i] = min(dat[i * 2 + 1], dat[i * 2 + 2])

def query(a, b, k, l, r):
    global dat, m
    if r <= a or b <= l:
        return 2 ** 31 - 1
    if a <= l and r <= b:
        return dat[k]
    else:
        vl = query(a, b, k * 2 + 1, l, (l + r) // 2)
        vr = query(a, b, k * 2 + 2, (l + r) // 2, r)
        return min(vl, vr)

n, q = map(int, input().split())
m = 1

while m < n:
    m *= 2

init()

for _ in range(q):
    com, x, y = map(int, input().split())
    if com == 0:
        update(x, y)
    else:
        print(query(x, y + 1, 0, 0, m))

