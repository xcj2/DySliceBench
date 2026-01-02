def cross(c1, c2):
    return c1.real * c2.imag - c1.imag * c2.real

def ccw(p0, p1, p2):
    if cross(p1 - p0, p2 - p0) > 0:
        return True
    else:
        False

# Andrew's algorithm
import collections

def andrew(point_list):
    point_list.sort(key = lambda c: (c.imag, c.real))
    point_que = collections.deque(point_list)
    convex_hull = []
    rest_points = []
    start_point = point_que.popleft()

    # outward
    convex_hull.append(start_point)
    convex_hull.append(point_que.popleft())

    while point_que:
        new_point = point_que.popleft()
        while ccw(convex_hull[-1], convex_hull[-2], new_point):
            rest_points.append(convex_hull.pop())
            if len(convex_hull) == 1:
                break
        convex_hull.append(new_point)

    # homeward
    rest_points.append(start_point)
    rest_points.sort(key = lambda c: c.imag)

    while rest_points:
        new_point = rest_points.pop()
        while ccw(convex_hull[-1], convex_hull[-2], new_point):
            convex_hull.pop()
        convex_hull.append(new_point)

    # output
    convex_hull.pop()
    print(len(convex_hull))
    for p in convex_hull:
        print("{0:.0f} {1:.0f}".format(p.real, p.imag))

# Acceptance of input
def string_to_complex(s):
    x, y = map(int, s.split())
    return x + y * 1j

import sys

file_input = sys.stdin

n = int(file_input.readline())

P = [string_to_complex(file_input.readline()) for i in range(n)]

# solve
andrew(P)