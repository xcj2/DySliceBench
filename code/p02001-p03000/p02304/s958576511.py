import math

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    
    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other.y)
    
    def __mul__(self,scalar):
        return Vector(self.x*scalar,self.y*scalar)
    def __rmul__(self, scalar):
        return Vector(self.x*scalar,self.y*scalar)
    
   
    def __repr__(self):
        return str([self.x,self.y])
        
    def norm_2(self):
        return dot(self,self)
    
    def norm(self):
        return math.sqrt(self.norm_2())
    
def v_sum(v1,v2):
    return Vector(v1.x+v2.x,v1.y+v2.y) 
def scalar_multi(k,v):
    return Vector(k*v.x,k*v.y)
def v_diff(v1,v2):
    return v_sum(v1,scalar_multi(-1,v2))
    
def dot(vector1,vector2):
    return vector1.x*vector2.x+vector1.y*vector2.y

def cross(vector1,vector2):
    return vector1.x*vector2.y-vector1.y*vector2.x


import bisect

class EndPoint(Vector):
    def __init__(self,x,y,state):
        super().__init__(x,y)
        self.state = state
        '''
        state 0 bottom
        state 1 top
        state 2 left
        state 3 right
        '''
        return
    
class Segment:
    def __init__(self,p1,p2):
        if p1.x<p2.x:
            self.p1 = p1
            self.p2 = p2
        else:
            self.p1 = p2
            self.p2 = p1
        return
    
    
def sorting(p):
    if isinstance(p,Segment):
        return p.p1.y+0.1
    else:
        if p.state == 0:
            return p.y
        elif p.state == 1:
            return p.y+0.2
    
    
    

n = int(input())
points = []
for i in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    if x1 == x2:
        if y1<y2:
            points.append(EndPoint(x1,y1,0))
            points.append(EndPoint(x2,y2,1))
        else:
            points.append(EndPoint(x1,y1,1))
            points.append(EndPoint(x2,y2,0))
    else:
        if x1<x2:
            points.append(Segment(EndPoint(x1,y1,2),EndPoint(x2,y2,3)))
        else:
            points.append(Segment(EndPoint(x1,y1,3),EndPoint(x2,y2,2)))
        
points.sort(key = lambda x:sorting(x))

T = []
count = 0
for i in range(len(points)):
    if isinstance(points[i],Segment):
        left = bisect.bisect_left(T,points[i].p1.x)
        right = bisect.bisect_right(T,points[i].p2.x)
        count += right-left
    else:
        if points[i].state == 0:
            bisect.insort(T,points[i].x)
        elif points[i].state == 1:
            index=bisect.bisect_left(T,points[i].x)
            T.pop(index)

print(count)
