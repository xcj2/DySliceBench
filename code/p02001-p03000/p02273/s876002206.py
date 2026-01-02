#!/usr/bin/env python3
# -*- coding: utf-8 -*-


SIN60 = 0.86602540378
COS60 = 0.5


class KochCurve(object):

    def __init__(self, n, p1=(0.0, 0.0), p2=(100.0, 0.0)):
        self.depth = n
        self.p1_init = p1
        self.p2_init = p2
        self.points = [p1]

    def koch(self, n=None, p1=None, p2=None):
        if n is None:
            n = self.depth
        if p1 is None:
            p1 = self.p1_init
        if p2 is None:
            p2 = self.p2_init
        if n != 0:
            s = ((2 * p1[0] + p2[0]) / 3, (2 * p1[1] + p2[1]) / 3)
            t = ((p1[0] + 2 * p2[0]) / 3, (p1[1] + 2 * p2[1]) / 3)
            ux = (t[0] - s[0]) * COS60 - (t[1] - s[1]) * SIN60 + s[0]
            uy = (t[0] - s[0]) * SIN60 + (t[1] - s[1]) * COS60 + s[1]
            u = (ux, uy)
            self.koch(n - 1, p1, s)
            self.points.append(s)
            self.koch(n - 1, s, u)
            self.points.append(u)
            self.koch(n - 1, u, t)
            self.points.append(t)
            self.koch(n - 1, t, p2)

    def draw_koch(self):
        self.koch()
        self.points.append(self.p2_init)


def main():
    k = KochCurve(n=int(input()))
    k.draw_koch()
    for p in k.points:
        print("{x:.8f} {y:.8f}".format(x=p[0], y=p[1]))


if __name__ == "__main__":
    main()