# Aizu Problem CGL_2_B: Intersection
#
import sys, math, os

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


n = int(input())
for k in range(n):
    x1, y1, x2, y2, x3, y3, x4, y4 = [int(_) for _ in input().split()]
    print(1 if do_intersect([x1, y1], [x2, y2], [x3, y3], [x4, y4]) else 0)