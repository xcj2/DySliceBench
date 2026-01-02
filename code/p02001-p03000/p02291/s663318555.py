import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,a):
        return self.__class__(self.x+a.x,self.y+a.y)

    def __sub__(self,a):
        return self.__class__(self.x-a.x,self.y-a.y)

    def __mul__(self,d):
        return self.__class__(self.x*d,self.y*d)

    def __truediv__(self,d):
        return self.__class__(self.x/d,self.y/d)

    def __str__(self):
        return '%.10f %.10f'%(self.x,self.y)

    def abs(self):
        return self.norm()**(1.0/2.0)

    def norm(self):
        return (self.x*self.x+self.y*self.y)

    def rotate(self,d):
        r = math.pi*d/180.0
        return self.__class__( self.x*math.cos(r)-self.y*math.sin(r),
                               self.x*math.sin(r)+self.y*math.cos(r))

    def dot(self,p):
        return (self.x*p.x+self.y*p.y)

class Segment:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

def project(s,p):
    v = s.p2-s.p1
    r = v.dot(p-s.p1)/v.norm()
    return s.p1+v*r

def reflect(s,p):
    return p+(project(s,p)-p)*2.0

def main():
    a,b,c,d = map(float,input().split())
    s = Segment(Point(a,b),Point(c,d))
    q = int(input())
    for _ in range(q):
        e,f = map(float,input().split())
        p = Point(e,f)
        print (reflect(s,p))


if __name__ == '__main__':
    main()


