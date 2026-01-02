from math import sqrt

def cross(p0, p1, p2):
  x0, y0 = p0
  x1, y1 = p1
  x2, y2 = p2
  x1 -=x0
  x2 -=x0
  y1 -=y0
  y2 -=y0
  return x1*y2 - x2*y1

def dot(p0, p1, p2):
  x0, y0 = p0
  x1, y1 = p1
  x2, y2 = p2
  x1 -=x0
  x2 -=x0
  y1 -=y0
  y2 -=y0
  return x1*x2 + y1*y2

def dist2(p0, p1):
  x0, y0 = p0
  x1, y1 = p1
  return (x1-x0)**2 + (y1 - y0)**2

def collision_ll(s0, s1,t0,t1):
  return cross(s0, s1,t0)*cross(s0,s1,t1)<0 and cross(t0, t1,s0) * cross(t0,t1,s1) < 0

def dist_lp(S,E,P):
  dd = dist2(S,E)
  if 0 <= dot(S,E,P) <= dd:
    return abs(cross(S,E,P))/sqrt(dd)
  return sqrt(min(dist2(S,P), dist2(E,P)))

def dist_ll(s0, s1, t0, t1):
  if collision_ll(s0,s1,t0,t1):
    return 0
  return min(
    dist_lp(s0, s1, t0),
    dist_lp(s0, s1, t1),
    dist_lp(t0, t1, s0),
    dist_lp(t0, t1, s1)
    )

n = int(input())
for i in range(n):
  x0,y0,x1,y1,X0,Y0,X1,Y1 = map(int,input().split())
  print("%.010f"%dist_ll((x0,y0), (x1,y1), (X0,Y0),(X1,Y1)))

