def cross3(O, A, B):
    ox, oy = O; ax, ay = A; bx, by = B
    return (ax - ox) * (by - oy) - (bx - ox) * (ay - oy)
def outer(x0, y0, x1, y1):
    return x0*y1 - x1*y0
def is_intersection(P0, P1, Q0, Q1):
    C0 = cross3(P0, P1, Q0)
    C1 = cross3(P0, P1, Q1)
    D0 = cross3(Q0, Q1, P0)
    D1 = cross3(Q0, Q1, P1)
    if C0 == C1 == 0:
        return 0
    return C0 * C1 <= 0 and D0 * D1 <= 0
def cross_point(P0, Q0, P1, Q1):
    x0, y0 = P0; x1, y1 = Q0
    x2, y2 = P1; x3, y3 = Q1
    dx0 = x1 - x0
    dy0 = y1 - y0
    dx1 = x3 - x2
    dy1 = y3 - y2

    s = (y0-y2)*dx1 - (x0-x2)*dy1
    sm = dx0*dy1 - dy0*dx1
    if s < 0:
        s = -s
        sm = -sm
    if s == 0:
        x = x0
        y = y0
    else:
        x = x0 + s*dx0/sm
        y = y0 + s*dy0/sm
    return x, y
while 1:
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == y1 == x2 == y2 == 0:
        break
    P1 = (x1, y1); Q1 = (x2, y2)
    x3, y3, x4, y4 = map(int, input().split())
    P2 = (x3, y3); Q2 = (x4, y4)
    x5, y5, x6, y6 = map(int, input().split())
    P3 = (x5, y5); Q3 = (x6, y6)
    if (not is_intersection(P1, Q1, P2, Q2)
            or not is_intersection(P2, Q2, P3, Q3)
            or not is_intersection(P3, Q3, P1, Q1)):
        print("kyo")
        continue
    p1, q1 = cross_point(P1, Q1, P2, Q2)
    p2, q2 = cross_point(P2, Q2, P3, Q3)
    p3, q3 = cross_point(P3, Q3, P1, Q1)
    S = abs(outer(p2-p1, q2-q1, p3-p1, q3-q1)) / 2.
    if S < 1e-9:
        print("kyo")
    elif S < 100000:
        print("syo-kichi")
    elif S < 1000000:
        print("kichi")
    elif S < 1900000:
        print("chu-kichi")
    else:
        print("dai-kichi")
