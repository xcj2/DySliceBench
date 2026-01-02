from sys import stdin
readline = stdin.readline



def main():
    q = int(readline())
    for i in range(q):
        xy = map(int, readline().split())
        p0, p1, p2, p3 = [x + y * 1j for x, y in zip(*[xy] * 2)]
        print('{:.10f}'.format(distance(p0, p1, p2, p3)))

def lt(a, b):
    if a.real != b.real:
        return a.real <= b.real
    return a.imag < b.imag
import itertools
def distance(p0, p1, p2, p3):
    if is_intersected_ls(p0, p1, p2, p3):
        return 0
    p = []
    for i, j in itertools.product([p0, p1], [p2, p3]):
        p.append(abs(i - j))
    for i,j,k in [(p0,p1,p2),(p0,p1,p3),(p2,p3,p0),(p2,p3,p1)]:
        tmp = intersection_of_perpendicular(i,j,k)
        if (lt(i, tmp) and lt(tmp, j)) or (lt(j, tmp) and lt(tmp, i)):
            p.append(abs(tmp - k))

    return min(p)

# line(p1, p2) point(p3)
def intersection_of_perpendicular(p1, p2, p3):
    return p1 + (p2 - p1) * projecter(p2 - p1, p3 - p1)
 
 
def projecter(a, b):
    return dot(a, b) / dot(a, a)
 
 
def dot(a, b):
    return a.real * b.real + a.imag * b.imag


def is_intersected_ls(a1, a2, b1, b2):
    eps = 0
    if max(a1.real, a2.real) < min(b1.real, b2.real)\
      or max(b1.real, b2.real) < min(a1.real, a2.real)\
      or max(a1.imag, a2.imag) < min(b1.imag, b2.imag)\
      or max(b1.imag, b2.imag) < min(a1.imag, a2.imag):
        return False
    return (cross(a2-a1, b1-a1) * cross(a2-a1, b2-a1) <= eps)\
        and (cross(b2-b1, a1-b1) * cross(b2-b1, a2-b1) <= eps)

# http://imagingsolution.blog107.fc2.com/blog-entry-137.html
def intersection(p1, p2, p3, p4):
    a1 = p4 - p2
    b1 = p2 - p3
    b2 = p1 - p2
    s1 = cross(a1, b2) / 2
    s2 = cross(a1, b1) / 2
    c1 = p1 + (p3 - p1) * s1 / (s1 + s2)
    return c1


def cross(a, b):
    return a.real * b.imag - a.imag * b.real
main()