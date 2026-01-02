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

    def dot(self,p)  :return (self.x*p.x+self.y*p.y)
    def cross(self,p):return (self.x*p.y-self.y*p.x)

class Segment:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def __init__(self,a,b,c,d):
        self.p1 = Point(a,b)
        self.p2 = Point(c,d)

    def parallel(self,s):
        v1 = self.p2-self.p1
        v2 = s.p2-s.p1
        return v1.cross(v2)==0.0

    def orthogonal(self,s):
        v1 = self.p2-self.p1
        v2 = s.p2-s.p1
        return v1.dot(v2)==0.0

def project(s,p):
    v = s.p2-s.p1
    r = v.dot(p-s.p1)/v.norm()
    return s.p1+v*r

def reflect(s,p):
    return p+(project(s,p)-p)*2.0

def main():
    q = int(input())
    for _ in range(q):
        a,b,c,d,e,f,g,h = map(float,input().split())
        s = Segment(a,b,c,d)
        t = Segment(e,f,g,h)
        if s.parallel(t):print (2)
        elif s.orthogonal(t):print (1)
        else :print (0)

if __name__ == '__main__':
    main()


