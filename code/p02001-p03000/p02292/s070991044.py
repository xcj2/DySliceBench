from sys import stdin
readline = stdin.readline



def lt(a, b):
    if a.real != b.real:
        return a.real < b.real
    return a.imag < b.imag


def main():
    x1, y1, x2, y2 = map(int, readline().split())
    p1, p2 = x1 + y1 * 1j, x2 + y2 * 1j
    q = int(readline())
    for i in range(q):
        xi, yi = map(int, readline().split())
        pi = xi + yi * 1j

        s = cross(p2 - p1, pi - p1)
        if abs(s) < 1e-10:
            if (lt(p1, p2) and lt(p2, pi)) or (lt(pi, p2) and lt(p2, p1)):
                print('ONLINE_FRONT')
            elif (lt(pi, p1) and lt(p1, p2)) or (lt(p2, p1) and lt(p1, pi)):
                print('ONLINE_BACK')
            else:
                print('ON_SEGMENT')
        elif s < 0:
            print('CLOCKWISE')
        else:
            print('COUNTER_CLOCKWISE')


def projecter(a, b):
    return dot(a, b) / dot(a, a)


def dot(a, b):
    return a.real * b.real + a.imag * b.imag


def cross(a, b):
    return a.real * b.imag - a.imag * b.real
main()