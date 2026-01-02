# Aizu Problem 0068: Enclose Pins with a Rubber Band
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

while True:
    N = int(input())
    if N == 0:
        break
    points = [[float(_) for _ in input().split(',')] for __ in range(N)]
    print(N - (len(jarvis(points)) - 1))