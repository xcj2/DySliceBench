import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def Cp(p1, p2, p3):
    xa = p1.x-p2.x
    ya = p1.y-p2.y
    xb = p3.x-p2.x
    yb = p3.y-p2.y
    return xa*yb-ya*xb

def get_input():
    while True:
        try:
            yield ''.join(input())
        except EOFError:
            break

N = list(get_input())
for l in range(len(N)):

    x1,y1,x2,y2,x3,y3,x4,y4 = [float(i) for i in N[l].split(",")]

    p1 = Point(x1,y1)
    p2 = Point(x2,y2)
    p3 = Point(x3,y3)
    p4 = Point(x4,y4)

    cp1 = Cp(p1,p2,p3)
    cp2 = Cp(p2,p3,p4)
    cp3 = Cp(p3,p4,p1)
    cp4 = Cp(p4,p1,p2)

    if cp1 > 0 and cp2 > 0 and cp3 > 0 and cp4 > 0:
        print("YES")
    elif cp1 < 0 and cp2 < 0 and cp3 < 0 and cp4 < 0:
        print("YES")
    else:
        print("NO")

