import math

EPS = 1e-10


class Vector2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, v):
        return Vector2(self.x+v.x, self.y+v.y)

    def __sub__(self, v):
        return Vector2(self.x-v.x, self.y-v.y)

    def __mul__(self, v):
        return Vector2(self.x*v, self.y*v)

    def __truediv__(self, v):
        return Vector2(self.x/v, self.y/v)

    def __abs__(self):
        return math.sqrt(float(self.x*self.x+self.y*self.y))

    def __str__(self):
        return f"({self.x},{self.y})"

    def __lt__(self, v):
        if math.isclose(self.x, v.x):
            return self.y < v.y
        return self.x < v.x

    def dot(self, v):
        return self.x*v.x+self.y*v.y

    def cross(self, v):
        return self.x*v.y-self.y*v.x

    def norm(self):
        d = abs(self)
        return Vector2(self.x/d, self.y/d)


def projection(v1, v2, p):
    v12 = (v2-v1).norm()
    v1p = p-v1
    d = v12.dot(v1p)
    return v1+v12*d


def distanceLP(v1, v2, p):
    '''
    v1 -> v2の直線とpとの距離
    '''
    return abs((v2-v1).cross(p-v1))/abs(v2-v1)


def distanceSP(v1, v2, p):
    '''
    v1 -> v2の線分とpとの距離
    '''
    if (v2-v1).dot(p-v1) < 0.0:
        return abs(p-v1)
    if (v1-v2).dot(p-v2) < 0.0:
        return abs(p-v2)
    return distanceLP(v1, v2, p)


def ccw(p0, p1, p2):
    c = (p1-p0).cross(p2-p0)
    if math.isclose(c, 0.0, abs_tol=EPS):
        d = (p1-p0).dot(p2-p0)
        if d < 0.0:
            return -1
        else:
            d1 = abs(p1-p0)
            d2 = abs(p2-p0)
            if d1 < d2:
                return 1
            else:
                return 0
    elif c < 0.0:
        return -1
    else:
        return 1


def intersect(p1, p2, p3, p4):
    '''
    p1p2とp3p4の交差判定
    '''
    #t1 = (p1.x-p2.x)*(p3.y-p1.y)+(p1.y-p2.y)*(p1.x-p3.x)
    #t2 = (p1.x-p2.x)*(p4.y-p1.y)+(p1.y-p2.y)*(p1.x-p4.x)
    #t3 = (p3.x-p4.x)*(p1.y-p3.y)+(p3.y-p4.y)*(p3.x-p1.x)
    #t4 = (p3.x-p4.x)*(p2.y-p3.y)+(p3.y-p4.y)*(p3.x-p2.x)
    # return (t1*t2) <= 0.0 and (t3*t4) <= 0.0
    c1 = ccw(p1, p2, p3)*ccw(p1, p2, p4)
    c2 = ccw(p3, p4, p1)*ccw(p3, p4, p2)
    return c1 <= 0.0 and c2 <= 0.0


def distance(a1, a2, b1, b2):
    '''
    線分a1a2とb1b2の距離
    '''
    if intersect(a1, a2, b1, b2):
        return 0.0
    return min([
        min([distanceSP(a1, a2, b1), distanceSP(a1, a2, b2)]),
        min([distanceSP(b1, b2, a1), distanceSP(b1, b2, a2)])
    ])


n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
q = int(input())
p = [list(map(int, input().split())) for _ in range(q)]

for pi in p:
    pv = Vector2(pi[0], pi[1])

    '''
    多角形の内包判定
    右に大きく線分を引いて、線分と奇数回ぶつかる -> 内包
    or
    多角形を構成する線分上にある
    '''
    ans = None
    x = False
    for i in range(n):
        a = Vector2(g[i][0], g[i][1]) - pv
        b = Vector2(g[(i+1) % n][0], g[(i+1) % n][1]) - pv
        # a,b上に点pがある
        if math.isclose(abs(a.cross(b)), 0.0) and a.dot(b) < EPS:
            ans = "1"
            break
        else:
            # yが小さい順に入れ替える
            if a.y > b.y:
                a, b = b, a
            # a->bが反時計回りで、a.yとb.yの間にp(0.0)がある
            if a.cross(b) > EPS and a.y < EPS and b.y > EPS:
                x = not x
    if ans == None:
        ans = "2" if x else "0"
    print(ans)

