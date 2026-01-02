from sys import stdin
import operator
readline = stdin.readline


def cross(a, b):
    return a.real * b.imag - a.imag * b.real


def dot(a, b):
    return a.real * b.real + a.imag * b.imag


def ccw(a, b, c):
    b -= a
    c -= a
    if cross(b, c) > 0:  # counter clockwise
        return 1
    elif cross(b, c) < 0:  # clockwise
        return -1
    elif dot(b, c) < 0:  # c--a--b on line
        return -2
    elif abs(b) < abs(c):  # a--b--c on line
        return 2
    return 0


# http://www.prefield.com/algorithm/geometry/convex_hull.html
def convex_hull(ps):
    n = len(ps)
    k = 0
    ps.sort(key=operator.attrgetter('imag'))
    ch = [None] * 2 * n
    # lower-hull
    for i in range(n):
        while k >= 2 and ccw(ch[k-2], ch[k-1], ps[i]) <= 0:
            k -= 1
        ch[k] = ps[i]
        k += 1
    # upper-hull
    t = k + 1
    for i in reversed(range(n - 1)):
        while k >= t and ccw(ch[k-2], ch[k-1], ps[i]) <= 0:
            k -= 1
        ch[k] = ps[i]
        k += 1
    return ch[:k - 1]


n = int(readline())
p = [map(int, readline().split()) for _ in range(n)]
p = [x + y * 1j for x, y in p]

p = convex_hull(p)
print(len(p))
for pi in p:
    print(int(pi.real), int(pi.imag))