#!/usr/bin/env python3
# DSL_4_A: Union of Rectangles
# O(N^2)


class Rect:
    def __init__(self, p1, p2):
        self.top_left = p1
        self.bottom_right = p2

    def intersect(self, other):
        xs1, ys1 = self.top_left
        xs2, ys2 = self.bottom_right
        xo1, yo1 = other.top_left
        xo2, yo2 = other.bottom_right

        if xs1 >= xo2:
            return False
        elif xs2 <= xo1:
            return False

        if ys1 >= yo2:
            return False
        elif ys2 <= yo1:
            return False

        return True

    def sub(self, other):
        # assert self.intersect(other), "{} {}".format(self, other)
        xs1, ys1 = self.top_left
        xs2, ys2 = self.bottom_right
        xo1, yo1 = other.top_left
        xo2, yo2 = other.bottom_right
        if xs1 < xo1:
            yield Rect((xs1, ys1), (xo1, ys2))
        if xs2 > xo2:
            yield Rect((xo2, ys1), (xs2, ys2))
        if ys1 < yo1:
            yield Rect((max(xs1, xo1), ys1), (min(xs2, xo2), yo1))
        if ys2 > yo2:
            yield Rect((max(xs1, xo1), yo2), (min(xs2, xo2), ys2))

    def area(self):
        x1, y1 = self.top_left
        x2, y2 = self.bottom_right
        return (x2 - x1) * (y2 - y1)

    def __str__(self):
        return '<Rect({}, {})>'.format(self.top_left, self.bottom_right)


class Rects:
    def __init__(self):
        self.rects = []

    def add(self, rect):
        rects = []
        for r in self.rects:
            if rect.intersect(r):
                rects.extend(r.sub(rect))
            else:
                rects.append(r)
        rects.append(rect)
        self.rects = rects
        # assert self.not_intersect(), self

    def area(self):
        return sum([r.area() for r in self.rects])

    def __str__(self):
        s = '<Rects('
        s += '\n       '.join(str(r) for r in self.rects)
        s += ')>'
        return s

    def not_intersect(self):
        for i in range(len(self.rects)-1):
            for j in range(i+1, len(self.rects)):
                if self.rects[i].intersect(self.rects[j]):
                    return False
        return True


def run():
    n = int(input())
    rects = Rects()
    for _ in range(n):
        x1, y1, x2, y2 = [int(i) for i in input().split()]
        rect = Rect((x1, y1), (x2, y2))
        rects.add(rect)

    print(rects.area())


if __name__ == '__main__':
    run()

