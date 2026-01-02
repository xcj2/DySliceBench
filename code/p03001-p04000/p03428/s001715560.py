"""
@ 凸包をつくる
    > 凸包内部の点に属する領域は、半径Rの円からするともはやないものとして考えて良い
    > というかこの多角形自体点として考えていい！
@ 凸包の頂点vについて
    > vの両隣との傾きだけあればよい
    > その間の角度 / 360が答え
"""

from math import gcd, atan, pi, degrees

def cross3(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

def convex_hull(ps):
    qs = []
    N = len(ps)
    for p in ps:
        # 一直線上で高々2点にする場合は ">=" にする
        while len(qs) > 1 and cross3(qs[-1], qs[-2], p) > 0:
            qs.pop()
        qs.append(p)
    t = len(qs)
    for i in range(N-2, -1, -1):
        p = ps[i]
        while len(qs) > t and cross3(qs[-1], qs[-2], p) > 0:
            qs.pop()
        qs.append(p)
    return qs

def tup_to_key(tup):
    x, y = tup
    x += 10 ** 7
    y += 10 ** 7
    x *= 10 ** 8
    return x + y

def key_to_tup(key):
    x, y = divmod(key, 10 ** 8)
    x -= 10 ** 7
    y -= 10 ** 7
    return x, y

def angle(x1, y1, x2, y2):
    if y1 == y2:
        return pi / 2
    return atan(-(x1 - x2) / (y1 - y2))

def on_line(ps):
    st = set()
    for p, q in zip(ps, ps[1:]):
        px, py = p
        qx, qy = q
        dx, dy = qx - px, qy - py
        g = gcd(dx, dy)
        dx //= g
        dy //= g
        st.add(tup_to_key((dx, dy)))
    return len(st) == 1

if __name__ == "__main__":
    N = int(input())
    if N == 2:
        print(0.5)
        print(0.5)
        exit(0)

    res = dict()
    points = [list(map(int,input().split())) for _ in range(N)]

    # ps = sorted(points)
    # for a, b in zip(ps, ps[1:]):
    #     x1, y1 = a
    #     x2, y2 = b
    #     x, y = x2 - x1, y2 - y1
    #     print(x, y)

    if on_line(sorted(points)):
        mn = min(points)
        mx = max(points)
        res[tup_to_key(mn)] = 0.5
        res[tup_to_key(mx)] = 0.5
    else:
        ps = convex_hull(sorted(points))[:-1]
        sz = len(ps)
        for i, (x, y) in enumerate(ps):
            key = tup_to_key((x, y))
            lx, ly = ps[i - 1]
            rx, ry = ps[(i + 1) % sz]
            la = angle(x, y, lx, ly)
            ra = angle(x, y, rx, ry)
            a = ra - la
            # a = min(a, 2 * pi - a)
            # print(x, y)
            # print(degrees(la), degrees(ra))
            if a < 0:
                a += pi
            # print(la, ra)
            res[key] = a / (2 * pi)

    for tup in points:
        key = tup_to_key(tup)
        if key in res:
            print(res[key])
        else:
            print(0)
