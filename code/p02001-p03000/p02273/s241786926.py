# coding: utf-8
import math as m
N = int(input())

# フラクタルのステップをnとする
# 端点p1, p2を与えてs, t, uを計算
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
def rotateX(s, t, theta):
    return m.cos(theta)*(t.x - s.x) - m.sin(theta)*(t.y - s.y) + s.x

def rotateY(s, t, theta):
    return m.sin(theta)*(t.x - s.x) + m.cos(theta)*(t.y - s.y) + s.y
    
def koch(n, p1, p2):
    if n == 0:
        return
    # p1, p2からs, t, uを求める
    s = Point((2*p1.x + p2.x)/3, (2*p1.y + p2.y)/3)
    t = Point((p1.x + 2*p2.x)/3, (p1.y + 2*p2.y)/3)
    u = Point(rotateX(s, t, m.pi/3), rotateY(s, t, m.pi/3))
    
    # 各辺に対しても同様にs, t, uを求める
    # printの順番に注意
    koch(n-1, p1, s)
    print("{0:.8f} {1:.8f}".format(s.x, s.y))
    koch(n-1, s, u)
    print("{0:.8f} {1:.8f}".format(u.x, u.y))
    koch(n-1, u, t)
    print("{0:.8f} {1:.8f}".format(t.x, t.y))
    koch(n-1, t, p2)

p1 = Point(0, 0)
p2 = Point(100, 0)
print("{0:.8f} {1:.8f}".format(p1.x, p1.y))
koch(N, p1, p2)
print("{0:.8f} {1:.8f}".format(p2.x, p2.y))