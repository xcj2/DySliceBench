import cmath
import itertools
import math
import os
import random
import sys

INF = float("inf")
PI = cmath.pi
TAU = cmath.pi * 2
EPS = 1e-8


class Point:
    """
    2次元空間上の点
    """

    # 反時計回り側にある
    CCW_COUNTER_CLOCKWISE = 1
    # 時計回り側にある
    CCW_CLOCKWISE = -1
    # 線分の後ろにある
    CCW_ONLINE_BACK = 2
    # 線分の前にある
    CCW_ONLINE_FRONT = -2
    # 線分上にある
    CCW_ON_SEGMENT = 0

    def __init__(self, x: float, y: float):
        self.c = complex(x, y)

    @property
    def x(self):
        return self.c.real

    @property
    def y(self):
        return self.c.imag

    @staticmethod
    def from_complex(c: complex):
        return Point(c.real, c.imag)

    @staticmethod
    def from_polar(r: float, phi: float):
        c = cmath.rect(r, phi)
        return Point(c.real, c.imag)

    def __add__(self, p):
        """
        :param Point p:
        """
        c = self.c + p.c
        return Point(c.real, c.imag)

    def __iadd__(self, p):
        """
        :param Point p:
        """
        self.c += p.c
        return self

    def __sub__(self, p):
        """
        :param Point p:
        """
        c = self.c - p.c
        return Point(c.real, c.imag)

    def __isub__(self, p):
        """
        :param Point p:
        """
        self.c -= p.c
        return self

    def __mul__(self, f: float):
        c = self.c * f
        return Point(c.real, c.imag)

    def __imul__(self, f: float):
        self.c *= f
        return self

    def __truediv__(self, f: float):
        c = self.c / f
        return Point(c.real, c.imag)

    def __itruediv__(self, f: float):
        self.c /= f
        return self

    def __repr__(self):
        return "({}, {})".format(round(self.x, 10), round(self.y, 10))

    def __neg__(self):
        c = -self.c
        return Point(c.real, c.imag)

    def __eq__(self, p):
        return abs(self.c - p.c) < EPS

    def __abs__(self):
        return abs(self.c)

    def __lt__(self, p):
        return self.x - p.x < -EPS or self.x - p.x < EPS and self.y - p.y < -EPS

    def __le__(self, p):
        return self.x - p.x < -EPS or self.x - p.x < EPS and self.y - p.y < EPS

    def __gt__(self, p):
        return self.x - p.x > EPS or self.x - p.x > -EPS and self.y - p.y > EPS

    def __ge__(self, p):
        return self.x - p.x > EPS or self.x - p.x > -EPS and self.y - p.y > -EPS

    @staticmethod
    def ccw(a, b, c):
        """
        線分 ab に対する c の位置
        線分上にあるか判定するだけなら on_segment とかのが速い
        Verify: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_1_C&lang=ja
        :param Point a:
        :param Point b:
        :param Point c:
        """
        b = b - a
        c = c - a
        det = b.det(c)
        if det > EPS:
            return Point.CCW_COUNTER_CLOCKWISE
        if det < -EPS:
            return Point.CCW_CLOCKWISE
        if b.dot(c) < -EPS:
            return Point.CCW_ONLINE_BACK
        if b.dot(b - c) < -EPS:
            return Point.CCW_ONLINE_FRONT
        return Point.CCW_ON_SEGMENT

    def dot(self, p):
        """
        内積
        :param Point p:
        :rtype: float
        """
        return self.x * p.x + self.y * p.y

    def det(self, p):
        """
        外積
        :param Point p:
        :rtype: float
        """
        return self.x * p.y - self.y * p.x

    def dist(self, p):
        """
        距離
        :param Point p:
        :rtype: float
        """
        return abs(self.c - p.c)

    def norm(self):
        """
        原点からの距離
        :rtype: float
        """
        return abs(self.c)

    def phase(self):
        """
        原点からの角度
        :rtype: float
        """
        return cmath.phase(self.c)

    def angle(self, p, q):
        """
        p に向いてる状態から q まで反時計回りに回転するときの角度
        -pi <= ret <= pi
        :param Point p:
        :param Point q:
        :rtype: float
        """
        return (cmath.phase(q.c - self.c) - cmath.phase(p.c - self.c) + PI) % TAU - PI

    def area(self, p, q):
        """
        p, q となす三角形の面積
        :param Point p:
        :param Point q:
        :rtype: float
        """
        return -abs((p - self).det(q - self) / 2)

    def projection_point(self, p, q, allow_outer=False):
        """
        線分 pq を通る直線上に垂線をおろしたときの足の座標
        Verify: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_1_A&lang=ja
        :param Point p:
        :param Point q:
        :param allow_outer: 答えが線分の間になくても OK
        :rtype: Point|None
        """
        diff_q = q - p
        # 答えの p からの距離
        r = (self - p).dot(diff_q) / abs(diff_q)
        # 線分の角度
        phase = diff_q.phase()

        ret = Point.from_polar(r, phase) + p
        if allow_outer or (p - ret).dot(q - ret) < EPS:
            return ret
        return None

    def reflection_point(self, p, q):
        """
        直線 pq を挟んで反対にある点
        Verify: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_1_B&lang=ja
        :param Point p:
        :param Point q:
        :rtype: Point
        """
        # 距離
        r = abs(self - p)
        # pq と p-self の角度
        angle = p.angle(q, self)
        # 直線を挟んで角度を反対にする
        angle = (q - p).phase() - angle
        return Point.from_polar(r, angle) + p

    def on_segment(self, p, q, allow_side=True):
        """
        点が線分 pq の上に乗っているか
        Verify: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_1_C&lang=ja
        :param Point p:
        :param Point q:
        :param allow_side: 端っこでギリギリ触れているのを許容するか
        :rtype: bool
        """
        if not allow_side and (self == p or self == q):
            return False
        # 外積がゼロ: 面積がゼロ == 一直線
        # 内積がマイナス: p - self - q の順に並んでる
        return abs((p - self).det(q - self)) < EPS and (p - self).dot(q - self) < EPS

    @staticmethod
    def circumcenter_of(p1, p2, p3):
        """
        外心
        :param Point p1:
        :param Point p2:
        :param Point p3:
        :rtype: Point|None
        """
        if abs((p2 - p1).det(p3 - p1)) < EPS:
            # 外積がゼロ == 一直線
            return None
        # https://ja.wikipedia.org/wiki/外接円
        a = (p2.x - p3.x) ** 2 + (p2.y - p3.y) ** 2
        b = (p3.x - p1.x) ** 2 + (p3.y - p1.y) ** 2
        c = (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2
        num = p1 * a * (b + c - a) + p2 * b * (c + a - b) + p3 * c * (a + b - c)
        den = a * (b + c - a) + b * (c + a - b) + c * (a + b - c)
        return num / den

    @staticmethod
    def incenter_of(p1, p2, p3):
        """
        内心
        :param Point p1:
        :param Point p2:
        :param Point p3:
        """
        # https://ja.wikipedia.org/wiki/三角形の内接円と傍接円
        d1 = p2.dist(p3)
        d2 = p3.dist(p1)
        d3 = p1.dist(p2)
        return (p1 * d1 + p2 * d2 + p3 * d3) / (d1 + d2 + d3)


class Circle:
    def __init__(self, o, r):
        """
        :param Point o:
        :param float r:
        """
        self.o = o
        self.r = r

    def __eq__(self, other):
        return self.o == other.o and abs(self.r - other.r) < EPS

    def ctc(self, c):
        """
        共通接線 common tangent の数
        4: 離れてる
        3: 外接
        2: 交わってる
        1: 内接
        0: 内包
        inf: 同一
        Verify: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_7_A&lang=ja
        :param Circle c:
        :rtype: int
        """
        if self.o == c.o:
            return INF if abs(self.r - c.r) < EPS else 0
        # 円同士の距離
        d = self.o.dist(c.o) - self.r - c.r
        if d > EPS:
            return 4
        elif d > -EPS:
            return 3
        # elif d > -min(self.r, c.r) * 2:
        elif d + min(self.r, c.r) * 2 > EPS:
            return 2
        elif d + min(self.r, c.r) * 2 > -EPS:
            return 1
        return 0

    def has_point_on_edge(self, p):
        """
        指定した点が円周上にあるか
        :param Point p:
        :rtype: bool
        """
        return abs(self.o.dist(p) - self.r) < EPS

    def contains(self, p, allow_on_edge=True):
        """
        指定した点を含むか
        :param Point p:
        :param bool allow_on_edge: 辺上の点を許容するか
        """
        if allow_on_edge:
            # return self.o.dist(p) <= self.r
            return self.o.dist(p) - self.r < EPS
        else:
            # return self.o.dist(p) < self.r
            return self.o.dist(p) - self.r < -EPS

    def area(self):
        """
        面積
        """
        return self.r ** 2 * PI

    def circular_segment_area(self, angle):
        """
        弓形⌓の面積
        :param float angle: 角度ラジアン
        """
        # 扇形の面積
        sector_area = self.area() * angle / TAU
        # 三角形部分を引く
        return sector_area - self.r ** 2 * math.sin(angle) / 2

    def intersection_points(self, other, allow_outer=False):
        """
        :param Segment|Circle other:
        :param bool allow_outer:
        """
        if isinstance(other, Segment):
            return self.intersection_points_with_segment(other, allow_outer=allow_outer)
        if isinstance(other, Circle):
            return self.intersection_points_with_circle(other)
        raise NotImplementedError()

    def intersection_points_with_segment(self, s, allow_outer=False):
        """
        線分と交差する点のリスト
        Verify: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_7_D&lang=ja
        :param Segment s:
        :param bool allow_outer: 線分の間にない点を含む
        :rtype: list of Point
        """
        # 垂線の足
        projection_point = self.o.projection_point(s.p1, s.p2, allow_outer=True)
        # 線分との距離
        dist = self.o.dist(projection_point)
        # if dist > self.r:
        if dist - self.r > EPS:
            return []
        if dist - self.r > -EPS:
            if allow_outer or s.has_point(projection_point):
                return [projection_point]
            else:
                return []
        # 足から左右に diff だけ動かした座標が答え
        diff = Point.from_polar(math.sqrt(self.r ** 2 - dist ** 2), s.phase())
        ret1 = projection_point + diff
        ret2 = projection_point - diff
        ret = []
        if allow_outer or s.has_point(ret1):
            ret.append(ret1)
        if allow_outer or s.has_point(ret2):
            ret.append(ret2)
        return ret

    def intersection_points_with_circle(self, other):
        """
        円と交差する点のリスト
        Verify: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_7_E&langja
        :param circle other:
        :rtype: list of Point
        """
        ctc = self.ctc(other)
        if not 1 <= ctc <= 3:
            return []
        if ctc == 3:
            # 外接
            return [Point.from_polar(self.r, (other.o - self.o).phase()) + self.o]
        if ctc == 1:
            # 内接
            if self.r > other.r:
                return [Point.from_polar(self.r, (other.o - self.o).phase()) + self.o]
            else:
                return [Point.from_polar(self.r, (self.o - other.o).phase()) + self.o]
        # 2つ交点がある
        assert ctc == 2

        a = other.r
        b = self.r
        c = self.o.dist(other.o)
        # 余弦定理で cos(a) を求めます
        cos_a = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
        angle = math.acos(cos_a)
        phi = (other.o - self.o).phase()
        return [
            self.o + Point.from_polar(self.r, phi + angle),
            self.o + Point.from_polar(self.r, phi - angle),
        ]

    def tangent_points_with_point(self, p):
        """
        p を通る接線との接点
        :param Point p:
        :rtype: list of Point
        """
        dist = self.o.dist(p)
        # if dist < self.r:
        if dist - self.r < -EPS:
            # p が円の内部にある
            return []
        if dist - self.r < EPS:
            # p が円周上にある
            return [Point(p.x, p.y)]

        a = math.sqrt(dist ** 2 - self.r ** 2)
        b = self.r
        c = dist
        # 余弦定理で cos(a) を求めます
        cos_a = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
        angle = math.acos(cos_a)
        phi = (p - self.o).phase()
        return [
            self.o + Point.from_polar(self.r, phi + angle),
            self.o + Point.from_polar(self.r, phi - angle),
        ]

    def tangent_points_with_circle(self, other):
        """
        other との共通接線との接点
        :param Circle other:
        :rtype: list of Point
        """
        ctc = self.ctc(other)
        if ctc > 4:
            raise ValueError('2つの円が同一です')
        if ctc == 0:
            return []
        if ctc == 1:
            return self.intersection_points_with_circle(other)

        assert ctc in (2, 3, 4)
        ret = []
        # 共通外接線を求める
        # if self.r == other.r:
        if abs(self.r - other.r) < EPS:
            # 半径が同じ == 2つの共通外接線が並行
            phi = (other.o - self.o).phase()
            ret.append(self.o + Point.from_polar(self.r, phi + PI / 2))
            ret.append(self.o + Point.from_polar(self.r, phi - PI / 2))
        else:
            # 2つの共通外接線の交点から接線を引く
            intersection = self.o + (other.o - self.o) / (self.r - other.r) * self.r
            ret += self.tangent_points_with_point(intersection)

        # 共通内接線を求める
        # 2つの共通内接線の交点から接線を引く
        intersection = self.o + (other.o - self.o) / (self.r + other.r) * self.r
        ret += self.tangent_points_with_point(intersection)
        return ret

    @staticmethod
    def circumscribed_of(p1, p2, p3):
        """
        p1・p2・p3 のなす三角形の外接円
        Verify:
        :param Point p1:
        :param Point p2:
        :param Point p3:
        """
        if p1.on_segment(p2, p3):
            return Circle((p2 + p3) / 2, p2.dist(p3) / 2)
        if p2.on_segment(p1, p3):
            return Circle((p1 + p3) / 2, p1.dist(p3) / 2)
        if p3.on_segment(p1, p2):
            return Circle((p1 + p2) / 2, p1.dist(p2) / 2)
        o = Point.circumcenter_of(p1, p2, p3)
        return Circle(o, o.dist(p1))

    @staticmethod
    def min_enclosing(points):
        """
        points をすべて含む最小の円
        計算量の期待値は O(N)
        https://www.jaist.ac.jp/~uehara/course/2014/i481f/pdf/ppt-7.pdf
        Verify: https://www.spoj.com/problems/QCJ4/
        :param list of Point points:
        :rtype: Circle
        """
        points = points[:]
        random.shuffle(points)

        # 前から順番に決めて大きくしていく
        ret = Circle(points[0], 0)
        for i, p in enumerate(points):
            if ret.contains(p):
                continue
            ret = Circle(p, 0)
            for j, q in enumerate(points[:i]):
                if ret.contains(q):
                    continue
                # 2点を直径とする円
                ret = Circle((p + q) / 2, abs(p - q) / 2)
                for k, r in enumerate(points[:j]):
                    if ret.contains(r):
                        continue
                    # 3点に接する円
                    ret = Circle.circumscribed_of(p, q, r)
        return ret


class Line:
    """
    2次元空間上の直線
    """

    def __init__(self, a: float, b: float, c: float):
        """
        直線 ax + by + c = 0
        """
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def from_gradient(grad: float, intercept: float):
        """
        直線 y = ax + b
        :param grad: 傾き
        :param intercept: 切片
        :return:
        """
        return Line(grad, -1, intercept)

    @staticmethod
    def from_segment(p1, p2):
        """
        :param Point p1:
        :param Point p2:
        """
        a = p2.y - p1.y
        b = p1.x - p2.x
        c = p2.y * (p2.x - p1.x) - p2.x * (p2.y - p1.y)
        return Line(a, b, c)

    @property
    def gradient(self):
        """
        傾き
        """
        return INF if self.b == 0 else -self.a / self.b

    @property
    def intercept(self):
        """
        切片
        """
        return INF if self.b == 0 else -self.c / self.b

    def is_parallel_to(self, l):
        """
        平行かどうか
        Verify: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_2_A&lang=ja
        :param Line l:
        """
        # 法線ベクトル同士の外積がゼロ
        return abs(Point(self.a, self.b).det(Point(l.a, l.b))) < EPS

    def is_orthogonal_to(self, l):
        """
        直行しているかどうか
        Verify: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_2_A&lang=ja
        :param Line l:
        """
        # 法線ベクトル同士の内積がゼロ
        return abs(Point(self.a, self.b).dot(Point(l.a, l.b))) < EPS

    def intersection_point(self, l):
        """
        交差する点
        Verify: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_2_C&lang=ja
        :param Line l:
        :rtype: Point|None
        """
        a1, b1, c1 = self.a, self.b, self.c
        a2, b2, c2 = l.a, l.b, l.c
        det = a1 * b2 - a2 * b1
        if abs(det) < EPS:
            # 並行
            return None
        x = (b1 * c2 - b2 * c1) / det
        y = (a2 * c1 - a1 * c2) / det
        return Point(x, y)

    def dist(self, p):
        """
        他の点との最短距離
        :param Point p:
        """
        raise NotImplementedError()

    def has_point(self, p):
        """
        p が直線上に乗っているかどうか
        :param Point p:
        """
        return abs(self.a * p.x + self.b * p.y + self.c) < EPS


class Segment:
    """
    2次元空間上の線分
    """

    def __init__(self, p1, p2):
        """
        :param Point p1:
        :param Point p2:
        """
        self.p1 = p1
        self.p2 = p2

    def norm(self):
        """
        線分の長さ
        """
        return abs(self.p1 - self.p2)

    def phase(self):
        """
        p1 を原点としたときの p2 の角度
        """
        return (self.p2 - self.p1).phase()

    def is_parallel_to(self, s):
        """
        平行かどうか
        Verify: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_2_A&lang=ja
        :param Segment s:
        :return:
        """
        # 外積がゼロ
        return abs((self.p1 - self.p2).det(s.p1 - s.p2)) < EPS

    def is_orthogonal_to(self, s):
        """
        直行しているかどうか
        Verify: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_2_A&lang=ja
        :param Segment s:
        :return:
        """
        # 内積がゼロ
        return abs((self.p1 - self.p2).dot(s.p1 - s.p2)) < EPS

    def intersects_with(self, s, allow_side=True):
        """
        交差するかどうか
        Verify: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_2_B&lang=ja
        :param Segment s:
        :param allow_side: 端っこでギリギリ触れているのを許容するか
        """
        if self.is_parallel_to(s):
            # 並行なら線分の端点がもう片方の線分の上にあるかどうか
            return (s.p1.on_segment(self.p1, self.p2, allow_side) or
                    s.p2.on_segment(self.p1, self.p2, allow_side) or
                    self.p1.on_segment(s.p1, s.p2, allow_side) or
                    self.p2.on_segment(s.p1, s.p2, allow_side))
        else:
            # allow_side ならゼロを許容する
            det_upper = EPS if allow_side else -EPS
            ok = True
            # self の両側に s.p1 と s.p2 があるか
            ok &= (self.p2 - self.p1).det(s.p1 - self.p1) * (self.p2 - self.p1).det(s.p2 - self.p1) < det_upper
            # s の両側に self.p1 と self.p2 があるか
            ok &= (s.p2 - s.p1).det(self.p1 - s.p1) * (s.p2 - s.p1).det(self.p2 - s.p1) < det_upper
            return ok

    def closest_point(self, p):
        """
        線分上の、p に最も近い点
        :param Point p:
        """
        # p からおろした垂線までの距離
        d = (p - self.p1).dot(self.p2 - self.p1) / self.norm()
        # p1 より前
        if d < EPS:
            return self.p1
        # p2 より後
        if -EPS < d - self.norm():
            return self.p2
        # 線分上
        return Point.from_polar(d, (self.p2 - self.p1).phase()) + self.p1

    def dist(self, p):
        """
        他の点との最短距離
        :param Point p:
        """
        return abs(p - self.closest_point(p))

    def dist_segment(self, s):
        """
        他の線分との最短距離
        Verify: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_2_D&lang=ja
        :param Segment s:
        """
        if self.intersects_with(s):
            return 0.0
        return min(
            self.dist(s.p1),
            self.dist(s.p2),
            s.dist(self.p1),
            s.dist(self.p2),
        )

    def has_point(self, p, allow_side=True):
        """
        p が線分上に乗っているかどうか
        :param Point p:
        :param allow_side: 端っこでギリギリ触れているのを許容するか
        """
        return p.on_segment(self.p1, self.p2, allow_side=allow_side)


if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353


N, K = list(map(int, sys.stdin.buffer.readline().split()))
XYC = [list(map(int, sys.stdin.buffer.readline().split())) for _ in range(N)]

# 解説・解法2
# 2つまたは3つの肉が同時に焼ける点と時間を全部列挙

if K == 1:
    print(0)
    exit()

tp = []
# 2つ
for (x1, y1, c1), (x2, y2, c2) in itertools.combinations(XYC, r=2):
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    I = p1 + (p2 - p1) / (100 / c1 + 100 / c2) * 100 / c1
    t = p1.dist(I) * c1
    tp.append((t, I))


def same_ratio_circle(p1, p2, ratio1, ratio2):
    # 内側
    i = p1 + (p2 - p1) * ratio1 / (ratio1 + ratio2)
    # 外側
    o = p1 + (p2 - p1) * ratio1 / (ratio1 - ratio2)
    return Circle((i + o) / 2, i.dist(o) / 2)


# plot_figure(same_ratio_circle(Point(1, 1), Point(-1, 1), 2, 3))
# exit()

def intersection_points(f1, f2):
    if isinstance(f1, Circle):
        return f1.intersection_points(f2, allow_outer=True)
    elif isinstance(f2, Circle):
        return f2.intersection_points(f1, allow_outer=True)
    elif isinstance(f1, Segment) and isinstance(f2, Segment):
        ret = Line.from_segment(f1.p1, f1.p2).intersection_point(Line.from_segment(f2.p1, f2.p2))
        return [ret] if ret else []

    else:
        assert False


# 3つ
for (x1, y1, c1), (x2, y2, c2), (x3, y3, c3) in itertools.combinations(XYC, r=3):
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    p3 = Point(x3, y3)
    # p1, p2, p3 への距離の比が 1/c1 : 1/c2 : 1/c3 となる点 I を探します
    # 2点への距離の比が等しくなるような点の集合は、比が 1:1 のときは直線、それ以外のときは円になるので、
    # それらを構築して交点を調べる
    # https://math.nakaken88.com/textbook/basic-locus-distance-ratio-and-circle/

    figures = []
    for (p1, c1), (p2, c2) in itertools.combinations(((p1, c1), (p2, c2), (p3, c3)), 2):
        if c1 == c2:
            o = (p1 + p2) / 2
            figures.append(Segment(o, o + (p2 - p1) * 1j))
        else:
            figures.append(same_ratio_circle(p1, p2, 1 / c1, 1 / c2))
    # figures 3 つがすべて重なる点
    ps1 = intersection_points(figures[0], figures[1])
    ps2 = intersection_points(figures[1], figures[2])
    ps3 = intersection_points(figures[2], figures[0])
    Is = []
    for p in ps1 + ps2 + ps3:
        for q in ps1:
            if p == q:
                break
        else:
            break
        for q in ps2:
            if p == q:
                break
        else:
            break
        for q in ps3:
            if p == q:
                break
        else:
            break
        Is.append(p)
    # for p in ps1 + ps2 + ps3:
    #     print(p, p1.dist(p) * c1)
    while Is:
        I = Is.pop()
        t = p1.dist(I) * c1
        tp.append((t, I))
        # print('t', p1.dist(I) * c1, p2.dist(I) * c2, p3.dist(I) * c3, I)
        # plot_figure(
        #     Circle(p1, p1.dist(I)),
        #     Circle(p2, p2.dist(I)),
        #     Circle(p3, p3.dist(I)),
        #     Segment(p1, p2),
        #     Segment(p2, p3),
        #     Segment(p3, p1),
        # )
tp.sort()
# print(tp)
for t, p in tp:
    cnt = 0
    for x, y, c in XYC:
        cnt += Circle(Point(x, y), t / c).contains(p)
    if cnt >= K:
        print(t)
        break
