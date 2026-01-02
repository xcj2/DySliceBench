import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "{:.8f} {:.8f}".format(self.x, self.y)

class kochCurveController:
    def insertTriangle(self,p1, p2,d):
        if d == 0:
            return
        s = self.secret(p1,p2,1,2)
        t = self.secret(p1,p2,2,1)
        u = self.calcVertex(s,t)

        self.insertTriangle(p1,s,d-1)
        print(s)
        self.insertTriangle(s,u,d-1)
        print(u)
        self.insertTriangle(u,t,d-1)
        print(t)
        self.insertTriangle(t,p2,d-1)


    def calcVertex(self,s,t):
        x = t.x - s.x
        y = t.y - s.y
        return Point(s.x+math.cos(math.radians(60))*x -math.sin(math.radians(60))*y, s.y+math.sin(math.radians(60))*x+math.cos(math.radians(60))*y)

    def secret(self,va,vb,a,b):
        return Point((b*(va.x)+a*(vb.x))/(a+b),(b*(va.y)+a*(vb.y))/(a+b))


K = kochCurveController()
N = int(input())
print(Point(0,0))
K.insertTriangle(Point(0,0),Point(100,0),N)
print(Point(100,0))


