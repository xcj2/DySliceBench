N = int(input())
xyh = [tuple(int(i) for i in input().split()) for i in range(N)]


def H(cx, cy, x, y, h):
    return h + abs(x - cx) + abs(y - cy)


def g(l, cx, cy):
    H_max_l = set(H(cx, cy, x, y, h) for x, y, h in l if h == 0)
    h_max = min(H_max_l) if any(H_max_l) else -1
    
    TH = set(H(cx, cy, x, y, h) for x, y, h in l if h > 0)
    if len(TH) == 1:
        high = TH.pop()
        if h_max == -1 or high <= h_max:
            return high
    return -1


def f(l):
    for cx in range(0, 101):
        for cy in range(0, 101):
            h = g(l, cx, cy)
            if h > 0:
                return cx, cy, h

cx, cy, h = f(xyh)
print(cx, cy, h)
