import math

def cross(a,b): #外積
  return a.real*b.imag-a.imag*b.real

def dot(a,b): #内積
  return a.real*b.real+a.imag*b.imag

def norm2(a,b): #大きさの2乗
  return (b.real-a.real)**2+(b.imag-a.imag)**2

def is_intersect(p0,p1,p2,p3): #交差しているのかを判定
  ta=cross(p1-p0,p2-p0)
  tb=cross(p1-p0,p3-p0)
  tc=cross(p3-p2,p0-p2)
  td=cross(p3-p2,p1-p2)

  if ta*tb<0 and tc*td<0:
    return True
  else:
    return False

def distance_option(p0,p1,p2):
  nn=norm2(p0,p1)
  #print(dot(p1-p0,p2-p0),nn)
  if 0<=dot(p1-p0,p2-p0)<=nn:
    return abs(cross(p1-p0,p2-p0))/math.sqrt(nn)
  else:
    return math.sqrt(min(norm2(p0,p2),norm2(p1,p2)))

def distance(p0,p1,p2,p3):
  if is_intersect(p0,p1,p2,p3):
    return 0
  else:
    #print(distance_option(p0,p1,p2),distance_option(p0,p1,p3),distance_option(p2,p3,p0),distance_option(p2,p3,p1))
    return min(distance_option(p0,p1,p2),distance_option(p0,p1,p3),distance_option(p2,p3,p0),distance_option(p2,p3,p1))

q=int(input())

for _ in [0]*q:
  x_y=map(int,input().split())
  p0,p1,p2,p3=[x+y*1j for x,y in zip(*[x_y]*2)]
  print("{:.10f}".format(distance(p0,p1,p2,p3)))
