# Aizu Problem 0187: Stoning Fortune
#
import sys, math, os, bisect

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")

def on_segment(p, q, r):
    # Given three colinear points p, q, r, the function checks if
    # point q lies on line segment 'pr'
    return q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and \
           q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])

def orientation(p, q, r):
    # To find orientation of ordered triplet (p, q, r).
    # The function returns following values
    #   0 --> p, q and r are colinear
    #   1 --> Clockwise
    #   2 --> Counterclockwise
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2


def do_intersect(p1, q1, p2, q2):
    # The main function that returns true if line segment 'p1q1'
    # and 'p2q2' intersect.
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
    #
    # General case:
    if o1 != o2 and o3 != o4:
        return True
    #
    # Special Cases:
    # 
    # p1, q1 and p2 are colinear and p2 lies on segment p1q1
    if o1 == 0 and on_segment(p1, p2, q1):
        return True
    # p1, q1 and p2 are colinear and q2 lies on segment p1q1
    if o2 == 0 and on_segment(p1, q2, q1):
        return True
    # p2, q2 and p1 are colinear and p1 lies on segment p2q2
    if o3 == 0 and on_segment(p2, p1, q2):
        return True
    #  p2, q2 and q1 are colinear and q1 lies on segment p2q2
    if o4 == 0 and on_segment(p2, q1, q2):
        return True
    # Doesn't fall in any of the above cases:
    return False


def ip(xy1,xy2):
    ax,ay,bx,by = xy1; cx,cy,dx,dy = xy2
    dn = ((by-ay)*(dx-cx)-(bx-ax)*(dy-cy))*1.0
    x = ((cy*dx-cx*dy)*(bx-ax)-(ay*bx-ax*by)*(dx-cx))/dn
    y = ((cy*dx-cx*dy)*(by-ay)-(ay*bx-ax*by)*(dy-cy))/dn
    return x,y
 
def stoning_fortune(coord1, coord2, coord3):
    p1, q1 = coord1[:2], coord1[2:]
    p2, q2 = coord2[:2], coord2[2:]
    p3, q3 = coord3[:2], coord3[2:]
    if not do_intersect(p1, q1, p2, q2) or not do_intersect(p1, q1, p3, q3) or \
       not do_intersect(p3, q3, p2, q2) :
        return "kyo"
    x1, y1 = ip(coord1, coord2)
    x2, y2 = ip(coord2, coord3)
    x3, y3 = ip(coord3, coord1)
    area = abs(.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
    if area >= 1900000:
        return "dai-kichi"
    elif area >= 1000000:
        return "chu-kichi"
    elif area >= 100000:
        return "kichi"
    elif area > 0:
        return "syo-kichi"
    else:
        return "kyo"
    
    
while True:
    coord1 = [int(_) for _ in input().split()]
    if coord1 == [0, 0, 0, 0]:
        break
    coord2 = [int(_) for _ in input().split()]
    coord3 = [int(_) for _ in input().split()]
    print(stoning_fortune(coord1, coord2, coord3))