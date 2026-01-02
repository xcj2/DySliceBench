from sys import stdin
readline = stdin.readline


def main():
    q = int(readline())
    for i in range(q):
        xy = map(int, readline().split())
        p0, p1, p2, p3 = [x + y * 1j for x, y in zip(*[xy] * 2)]
        print(1 if is_intersected_ls(p0, p1, p2, p3) else 0)


def is_intersected_ls(a1, a2, b1, b2):
    eps = 0
    if max(a1.real, a2.real) < min(b1.real, b2.real)\
      or max(b1.real, b2.real) < min(a1.real, a2.real)\
      or max(a1.imag, a2.imag) < min(b1.imag, b2.imag)\
      or max(b1.imag, b2.imag) < min(a1.imag, a2.imag):
        return False

    #print(cross(a2-a1, b1-a1))
    #print(cross(a2-a1, b2-a1))
    #print(cross(b2-b1, a1-b1))
    #print(cross(b2-b1, a2-b1))
    return (cross(a2-a1, b1-a1) * cross(a2-a1, b2-a1) <= eps)\
        and (cross(b2-b1, a1-b1) * cross(b2-b1, a2-b1) <= eps)


def cross(a, b):
    return a.real * b.imag - a.imag * b.real
main()