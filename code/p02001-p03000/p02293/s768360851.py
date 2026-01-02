class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Vector(Point):
    pass

def point_to_vector(p1, p2):
    x = p1.x - p2.x
    y = p1.y - p2.y
    return Vector(x, y)

def dot(v1, v2):
    return v1.x * v2.x + v1.y * v2.y

def cross(v1, v2):
    return v1.x * v2.y - v1.y * v2.x

def is_orth(v1, v2):
    if dot(v1, v2) == 0:
        return True
    else:
        return False

def is_pal(v1, v2):
    if cross(v1, v2) == 0:
        return True
    else:
        return False

q = int(input())
for i in range(q):
    temp = list(map(int, input().split()))
    points = []
    for j in range(0, 8, 2):
        points.append(Point(temp[j], temp[j+1]))
    v1 = point_to_vector(points[0], points[1])
    v2 = point_to_vector(points[2], points[3])
    if is_pal(v1, v2):
        ans = 2
    elif is_orth(v1, v2):
        ans = 1
    else:
        ans = 0
    print(ans)
