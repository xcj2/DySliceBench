# coding: utf-8
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def drawKoch(p1, p2, N):
    s = Point((2*p1.x+p2.x)/3,(2*p1.y+p2.y)/3)
    t = Point((p1.x+2*p2.x)/3,(p1.y+2*p2.y)/3)
    xx = t.x - s.x
    yy = t.y - s.y
    u = Point(s.x + xx/2 - yy*math.sqrt(3)/2, s.y + xx*math.sqrt(3)/2 + yy/2)
    if N > 1:
        drawKoch(p1, s, N-1)
        drawKoch(s, u, N-1)
        drawKoch(u, t, N-1)
        drawKoch(t, p2, N-1)
    else:
        printPoint(p1)
        printPoint(s)
        printPoint(u)
        printPoint(t)

def printPoint(p):
    print("{0:.8f} {1:.8f}".format(p.x, p.y))

n = int(input().rstrip())
p1 = Point(0,0)
p2 = Point(100,0)
if n == 0:
    printPoint(p1)
    printPoint(p2)
else:
    drawKoch(p1, p2, n)
    printPoint(p2)
