import math,sys
try: sys.stdin = open('in.in','r')
except: pass

class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __add__(self,p):
		return Point(self.x+p.x,self.y+p.y)
	def __sub__(self,p):
		return Point(self.x-p.x,self.y-p.y)
	def __mul__(self,p):
		return Point(self.x*p,self.y*p)

def Dot(a,b):
	return a.x*b.x + a.y*b.y
def Cross(a,b):
	return a.x*b.y - a.y*b.x
def Dis(a,b):
	return math.sqrt( (a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y) )
def Dis2(a,b):
	return (a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y)

q = int(input())
for i in range(q):

	x0,y0,x1,y1,x2,y2,x3,y3 = map(int,input().split())
	p0 = Point(x0,y0)
	p1 = Point(x1,y1)
	p2 = Point(x2,y2)
	p3 = Point(x3,y3)

	l1 = p0-p1
	l2 = p3-p2

	if Dot(l1,l2) == 0:
		print('1')
	elif Cross(l1,l2) == 0:
		print('2')
	else:
		print('0')

