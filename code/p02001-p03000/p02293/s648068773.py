EPS = 0.0000000001

class Point:
    
    global EPS
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
        
    def __add__(a, b):
        s = a.x + b.x
        t = a.y + b.y
        return Point(s, t)
        
    def __sub__(a, b):
        s = a.x - b.x
        t = a.y - b.y
        return Point(s, t)
            
    def __mul__(self, a):
        s = a * self.x
        t = a * self.y
        return Point(s, t)
        
    def __truediv__(self, a):
        s = self.x / a
        t = self.y / a
        return Point(s, t)
            
            
            
            
    def norm(self):
        return self.x * self.x + self.y * self.y
        
    def abs(self):
        return self.norm() ** 0.5
            
    
            
            
    def __eq__(self, other):
        return abs(self.x - other.y) < self.EPS and abs(self.y - other.y) < self.EPS
            
            
            
    def dot(self, b):
        return self.x * b.x + self.y * b.y
        
    def cross(self, b):
        return self.x * b.y - self.y * b.x
    
    

def isOrthogonal(a, b):
    return a.dot(b) == 0

def isParallel(a,b):
    return a.cross(b) == 0


n = int(input())
for i in range(n):
    nums=list(map(int,input().split()))
    a = Point(nums[0] - nums[2], nums[1] - nums[3])
    b = Point(nums[4] - nums[6], nums[5] - nums[7])

    if isParallel(a,b):
        print(2)
    elif isOrthogonal(a, b):
        print(1)
    else:
        print(0)




























