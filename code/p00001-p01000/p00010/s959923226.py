# AOJ 0010 Circumscribed Circle of a Triangle
# Python3 2018.6.22 bal4u

import math
EPS = 1e-8

def cross(a, b):
	return a.real*b.imag - a.imag*b.real
def dist(a, b):
	return math.hypot(a.real-b.real, a.imag-b.imag)
	
# 両直線の交点
def crossPointLL(ln1, ln2):
	u = ln1[1]-ln1[0]
	v = ln2[1]-ln2[0]
	return ln1[0] + u*(cross(v, ln2[0]-ln1[0])/cross(v, u))

# 入力:３点座標、リターン:外接円の円心座標、半径を表すリスト
def circumscribed_circle(p1, p2, p3):
	p12 = (p1+p2)/2
	p23 = (p2+p3)/2
	ln1 = [p12, p12+(p1-p2)*complex(0, 1)]
	ln2 = [p23, p23+(p2-p3)*complex(0, 1)]
	c = crossPointLL(ln1, ln2)
	return [c, dist(c, p1)]

for i in range(int(input())):
	p = list(map(float, input().split()))
	p1 = complex(p[0], p[1])
	p2 = complex(p[2], p[3])
	p3 = complex(p[4], p[5])
	ans = circumscribed_circle(p1, p2, p3)
	print(format(ans[0].real+EPS, ".3f"), format(ans[0].imag+EPS, ".3f"), format(ans[1]+EPS, ".3f"))

