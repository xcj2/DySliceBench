# Aizu Problem 0035: Is it Convex?
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def is_to_the_left(p1, p2, p3):
    # determine whether point p3 is to the left from the line from p1 to p2
    position = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    return position < 0


def jarvis(points):
    # determine convex hull by Jarvis' algorithm:
    max_y = max([p[1] for p in points])
    pointOnHull = [p for p in points if p[1] == max_y][0]
    convex_hull = [pointOnHull]
    while len(convex_hull) == 1 or convex_hull[-1] != convex_hull[0]:
        p = convex_hull[-1]
        endpoint = points[0]
        for j in range(len(points)):
            if endpoint == pointOnHull or is_to_the_left(p, endpoint, points[j]):
                endpoint = points[j]
        pointOnHull = endpoint
        convex_hull.append(pointOnHull)
    return convex_hull[::-1]
    

def convex_hull(points):
    hull = jarvis(points)
    length = 0
    line2 = ""
    for i in range(len(hull) - 1):
        p1, p2 = hull[i], hull[i+1]
        line2 += "(" + str(p1[0]) + "," + str(p1[1]) + ") "
    line2 += "(" + str(hull[-1][0]) + "," + str(hull[-1][1]) + ")"
    print(line2)
    

while True:
    try:
        x1, y1, x2, y2, x3, y3, x4, y4 = [float(_) for _ in input().split(',')]
    except EOFError:
        break
    print("YES" if len(jarvis([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])) == 5 else "NO")