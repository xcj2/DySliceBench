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

x0,y0,x1,y1 = map(int,input().split())
p0 = Point(x0,y0)
p1 = Point(x1,y1)
q = int(input())
for i in range(q):
	x2,y2 = map(int,input().split())
	p2 = Point(x2,y2)

	cross = Cross(p1-p0,p2-p0)
	if cross > 0:
		print('COUNTER_CLOCKWISE')
	elif cross < 0:
		print('CLOCKWISE')
	else:
		dot = Dot(p1-p0,p2-p0)
		if dot < 0:
			print('ONLINE_BACK')
		else:
			len1 = Dis2(p1,p0)
			len2 = Dis2(p2,p0)
			print( 'ONLINE_FRONT' if len1 < len2 else 'ON_SEGMENT' )

