def dot3(O, A, B):
  ox, oy = O
  ax, ay = A
  bx, by = B
  return (ax - ox) * (bx - ox) + (ay - oy) * (by - oy)

def cross3(O, A, B):
  ox, oy = O
  ax, ay = A
  bx, by = B
  return (ax - ox) * (by- oy) - (bx - ox) * (ay - oy)

def dist2(A, B):
  ax, ay = A
  bx, by = B
  return (ax - bx)**2 + (ay - by)**2

def is_intersection(p0, p1, q0, q1):
  c0 = cross3(p0, p1, q0)
  c1 = cross3(p0, p1, q1)
  d0 = cross3(q0, q1, p0)
  d1 = cross3(q0, q1, p1)
  if c0 == c1 == 0:
    e0 = dot3(p0, p1, q0)
    e1 = dot3(p0, p1, q1)
    if not e0 < e1:
      e0, e1 = e1, e0
    return e0 <= dist2(p0, p1) and 0 <= e1
  return c0 * c1 <= 0 and d0 * d1 <= 0

for q in range(int(input())):
  x0, y0, x1, y1, x2, y2, x3, y3 = map(int, input().split())
  print(+is_intersection((x0, y0), (x1, y1), (x2, y2), (x3, y3)))

