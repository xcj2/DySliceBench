from collections import defaultdict


def read_input():
    h, w, n = map(int, input().split())
    alist = []
    for i in range(n):
        (px, py) = map(int, input().split())
        alist.append((px, py))

    return h, w, n, alist


def count_arround(px, py, count):
    for xx in [-2, -1, 0]:
        for yy in [-2, -1, 0]:
            count[(px+xx, py+yy)] += 1


def is_area(p, h, w):
    if 1 <= p[0] <= h - 2:
        if 1 <= p[1] <= w - 2:
            return True
    return False


def submit():
    h, w, n, alist = read_input()

    count = defaultdict(int)

    for a in alist:
        count_arround(a[0], a[1], count)

    counts = count.items()
    counts = [c[1] for c in counts if is_area(c[0], h, w)]

    result = []
    s = 0
    for i in range(1, 10):
        result.append(sum([1 for c in counts if c == i]))
        s += result[-1]

    print((h - 2)*(w - 2) - s)
    for r in result:
        print(r)


if __name__ == '__main__':
    submit()
