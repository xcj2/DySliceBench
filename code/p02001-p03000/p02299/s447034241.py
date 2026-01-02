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

def is_crossed(p,far_point,s,t):
    a = far_point-p
    b = t-s
    v = s-p
    w = t-p
    x = p-s
    y = far_point-s
    if cross(a,v)*cross(a,w)<0 and cross(b,x)*cross(b,y)<0:
        return 0#'crossed on the edge'
    if cross(b,x) == 0 and 0<=dot(b,x)<=b.norm_2():
        return 1#'p on segment'
    if (cross(a,v)== 0 and 0<=dot(a,v)<=a.norm_2()) or (cross(a,w)==0 and 0<=dot(a,w)<=a.norm_2()):
        return 2#'crossed on the corner'
    return 3#not crossed

def polygon_content(point):
    insec_count = 0
    
    
    far_point = Vector(21001,21011) + point
    
    for i in range(n):
        judge = is_crossed(point,far_point,p[i-1],p[i])
        if judge==0:
            insec_count+=1
        elif judge==1:
            return 1
        elif judge==2:
            insec_count+=0.5
        
    if insec_count==0:
        return 0
    elif insec_count%2==0:
            return 0
    else:
        return 2

n = int(input())
p = []
for i in range(n):
    x,y = map(int,input().split())
    p.append(Vector(x,y))

q = int(input())
for i in range(q):
    x,y = map(int,input().split())
    print(polygon_content(Vector(x,y)))
