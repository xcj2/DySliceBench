from sys import stdin
readline = stdin.readline


def main():
    q = int(readline())
    for i in range(q):
        xy = map(int, readline().split())
        p0, p1, p2, p3 = [x + y * 1j for x, y in zip(*[xy] * 2)]
        c1 = intersection(p0, p2, p1, p3)
        print('{:.10f} {:.10f}'.format(c1.real, c1.imag))


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