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

def is_crossed(p,q,s,t):
    a = q-p
    b = t-s
    v = s-p
    w = t-p
    x = p-s
    y = q-s
    if cross(a,v)*cross(a,w)<=0 and cross(b,x)*cross(b,y)<=0:
        if cross(a,v) == cross(a,w) == cross(b,x) == cross(b,y) == 0:
            if 0<=dot(a,v)<=a.norm_2() or 0<=dot(a,w)<=a.norm_2()  or 0<=dot(b,x)<=b.norm_2() or 0<=dot(b,y)<=b.norm_2():
                return True
            else:
                return False
        else:    
            return True
    else:
        return False
        
q = int(input())
for i in range(q):
    x1,y1,x2,y2,x3,y3,x4,y4 = map(int,input().split())
    p1 = Vector(x1,y1)
    p2 = Vector(x2,y2)
    p3 = Vector(x3,y3)
    p4 = Vector(x4,y4)
    
    if is_crossed(p1,p2,p3,p4):
        print(1)
    else:
        print(0)
