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

def polygon_andrew_scan(points):
    u = []
    l = []
    if len(points)<3:
        return points
    points.sort(key = lambda p:p.x+p.y*10**-8)
    
    u.append(points[0])
    u.append(points[1])
    l.append(points[-1])
    l.append(points[-2])
    #from IPython.core.debugger import Pdb;
    #Pdb().set_trace()
    for i in range(2,len(points)):
        while len(u)>1 and cross(u[-2]-u[-1],points[i]-u[-1])<0:
            u.pop()
        u.append(points[i])
    #Pdb().set_trace()
    for i in range(2,len(points)):
        while len(l)>1 and cross(l[-2]-l[-1],points[-i-1]-l[-1])<0:
            l.pop()
        l.append(points[-i-1])
        
    return l[::-1]+u[1:-1][::-1]

n = int(input())
p = []

for i in range(n):
    x,y = map(int,input().split())
    p.append(Vector(x,y))
    
convex_points = polygon_andrew_scan(p)

bottom_l = convex_points[0]
start = 0
for i in range(len(convex_points)):
    if convex_points[i].y < bottom_l.y:
        bottom_l = convex_points[i]
        start = i
    elif convex_points[i].y == bottom_l.y:
        if convex_points[i].x<bottom_l.x:
            bottom_l = comvex_points[i]
            start = i
            
m = len(convex_points)      
print(m)
for i in range(start,start+m):
    print('{} {}'.format(convex_points[i%m].x,convex_points[i%m].y))
