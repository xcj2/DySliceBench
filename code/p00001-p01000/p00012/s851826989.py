import sys

def cross_product(a, b):
    ax, ay = a
    bx, by = b
    return ax * by - ay * bx


def sub(a, b):
    a1, a2 = a
    b1, b2 = b
    return b1 - a1, b2 - a2


def judge(p1, p2, p3, pp):

    cnt = 0
    for a, b in ((p1, p2), (p2, p3), (p3, p1)):
        vec1 = sub(a, b)
        vec2 = sub(a, pp)
        if cross_product(vec2, vec1) > 0:
            cnt += 1
    if cnt == 0 or cnt == 3:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    for line in sys.stdin:
        inputs = [float(s) for s in line.split()]
        p1 = (inputs.pop(0), inputs.pop(0))
        p2 = (inputs.pop(0), inputs.pop(0))
        p3 = (inputs.pop(0), inputs.pop(0))
        pp = (inputs.pop(0), inputs.pop(0))
        judge(p1, p2, p3, pp)
