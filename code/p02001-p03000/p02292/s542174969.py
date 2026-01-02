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


x1,y1,x2,y2 = map(float,input().split())
p1 = Vector(x1,y1)
p2 = Vector(x2,y2)

q = int(input())

for i in range(q):
    x,y = map(float,input().split())
    p3 = Vector(x,y)
    
    a = p2-p1
    v = p3-p1
    if cross(a,v) > 0:
        print('COUNTER_CLOCKWISE')
    elif cross(a,v) < 0:
        print('CLOCKWISE')
    else:
        if dot(a,v)<0:
            print('ONLINE_BACK')
        elif dot(a,v)>a.norm_2():
            print('ONLINE_FRONT')
        else:
            print('ON_SEGMENT')
