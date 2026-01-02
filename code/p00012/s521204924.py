import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def CP(p1, p2, p3):
    ax = p2.x-p1.x
    ay = p2.y-p1.y
    bx = p3.x-p1.x
    by = p3.y-p1.y
    return ax*by - ay*bx

def Judge(a,b,c):
    if a > 0 and b > 0 and c > 0:
        print("YES")
    elif a < 0 and b < 0 and c < 0:
        print("YES")
    else:
        print("NO")

def get_input():
    while True:
        try:
            yield ''.join(input())
        except EOFError:
            break

N = list(get_input())
for l in range(len(N)):
    x1,y1,x2,y2,x3,y3,xp,yp = [float(i) for i in N[l].split()]
    P1 = Point(x1,y1)
    P2 = Point(x2,y2)
    P3 = Point(x3,y3)
    PP = Point(xp,yp)

    cp1 = CP(PP, P1, P2)
    cp2 = CP(PP, P2, P3)
    cp3 = CP(PP, P3, P1)

    Judge(cp1,cp2,cp3)
