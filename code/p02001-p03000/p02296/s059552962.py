def cross(c1, c2):
    return c1.real * c2.imag - c1.imag * c2.real

def dot(c1, c2):
    return c1.real * c2.real + c1.imag * c2.imag

def ccw(p0, p1, p2):
    a = p1 - p0
    b = p2 - p0
    cross_ab = cross(a, b)
    if cross_ab > 0:
        return 1
    elif cross_ab < 0:
        return -1
    elif dot(a, b) < 0:
        return 1
    elif abs(a) < abs(b):
        return -1
    else:
        return 0

def intersect(p1, p2, p3, p4):
    # p1 and p2 are end points of a segment.
    # p3 and p4 are end points of the other segment.
    if (ccw(p1, p2, p3) * ccw(p1, p2, p4) <= 0) and \
       (ccw(p3, p4, p1) * ccw(p3, p4, p2) <= 0):
        return True
    else:
        return False

def get_distance_sp(sp1, sp2, p):
    a = sp2 - sp1
    b = p - sp1
    if dot(a, b) < 0:
        return abs(b)
    c = sp1 - sp2
    d = p - sp2
    if dot(c, d) < 0:
        return abs(d)
    return abs(cross(a, b)) / abs(a)

def print_distance(p1, p2, p3, p4):
    # parameters are the same as intersect.
    if intersect(p1, p2, p3, p4):
        print("0.0000000000")
    else:
        d = min(get_distance_sp(p1, p2, p3), get_distance_sp(p1, p2, p4),
                get_distance_sp(p3, p4, p1), get_distance_sp(p3, p4, p2))
        print("{0:.10f}".format(d))
        
n = int(input())
for line in range(n):
    x_p0, y_p0, x_p1, y_p1, x_p2, y_p2, x_p3, y_p3 = map(int, input().split())
    p0 = x_p0 + y_p0 * 1j
    p1 = x_p1 + y_p1 * 1j
    p2 = x_p2 + y_p2 * 1j
    p3 = x_p3 + y_p3 * 1j
    print_distance(p0, p1, p2, p3)

