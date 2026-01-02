def contain(x, y, r):
    return x**2 + y**2 <= r**2
def outer_p(x0, y0, x1, y1):
    return (x0*y1 - y0*x1)
def line_segment_circle(x0, y0, x1, y1, r, border=True):
    A = x0**2 + y0**2
    B = x0*x1 + y0*y1
    C = x1**2 + y1**2 - r**2
    D = B**2 - A*C
    if border:
        if D < 0:
            return 0
        if B <= 0 and B**2 > D:
            return 0
        if B - A >= 0 and (B - A)**2 > D:
            return 0
    else:
        if D <= 0:
            return 0
        if B <= 0 and B**2 >= D:
            return 0
        if B - A >= 0 and (B - A)**2 >= D:
            return 0
    return 1

while 1:
    x1, y1 = map(int, input().split())
    if x1 == y1 == 0:
        break
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    cx, cy = map(int, input().split())
    r = int(input())

    C1 = contain(x1-cx, y1-cy, r)
    C2 = contain(x2-cx, y2-cy, r)
    C3 = contain(x3-cx, y3-cy, r)
    if C1 and C2 and C3:
        print("b")
        continue
    if C1 or C2 or C3:
        print("c")
        continue
    p1 = outer_p(x2-x1, y2-y1, cx-x1, cy-y1)
    p2 = outer_p(x3-x2, y3-y2, cx-x2, cy-y2)
    p3 = outer_p(x1-x3, y1-y3, cx-x3, cy-y3)
    if 1 == (p1 < 0) == (p2 < 0) == (p3 < 0) or 1 == (p1 > 0) == (p2 > 0) == (p3 > 0):
        p1 = line_segment_circle(x2-x1, y2-y1, cx-x1, cy-y1, r, False)
        p2 = line_segment_circle(x3-x2, y3-y2, cx-x2, cy-y2, r, False)
        p3 = line_segment_circle(x1-x3, y1-y3, cx-x3, cy-y3, r, False)
        if p1 or p2 or p3:
            print("c")
        else:
            print("a")
        continue
    p1 = line_segment_circle(x2-x1, y2-y1, cx-x1, cy-y1, r, True)
    p2 = line_segment_circle(x3-x2, y3-y2, cx-x2, cy-y2, r, True)
    p3 = line_segment_circle(x1-x3, y1-y3, cx-x3, cy-y3, r, True)
    if p1 or p2 or p3:
        print("c")
        continue
    print("d")
