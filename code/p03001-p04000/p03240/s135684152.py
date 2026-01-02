def read():
    return int(input())


def readlist():
    return list(map(int, input().split()))


def readmap():
    return map(int, input().split())


N = read()
x = []
y = []
h = []
for i in range(N):
    xi, yi, hi = readmap()
    x.append(xi)
    y.append(yi)
    h.append(hi)
    if hi > 0:
       idx = i

for cx in range(101):
    for cy in range(101):
        H = h[idx] + abs(x[idx] - cx) + abs(y[idx] - cy)
        ok = True
        for i in range(N):
            if h[i] != max(0, H - abs(x[i] - cx) - abs(y[i] - cy)):
                ok = False
                break
        if ok:
            print(cx, cy, H)
            quit()
