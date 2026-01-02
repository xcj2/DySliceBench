import math

class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return "%.8f %.8f"%(self.x, self.y)


def koch(d, a, b):
	th = math.pi * 60.0 / 180.0
	if d == 0:
		return 0
	else:
		s = Point((2 * a.x + b.x) / 3.0, (2 * a.y + b.y) / 3.0)
		t = Point((a.x + 2 * b.x) / 3.0, (a.y + 2 * b.y) / 3.0)
		u = Point((t.x - s.x) * math.cos(th) - (t.y - s.y) * math.sin(th) + s.x,
							(t.x - s.x) * math.sin(th) + (t.y - s.y) * math.cos(th) + s.y)
		koch(d-1, a, s)
		print(s)
		koch(d-1, s, u)
		print(u)
		koch(d-1, u, t)
		print(t)
		koch(d-1, t, b)


if __name__ == "__main__":
	n = int(input())
	p1 = Point(0.0, 0.0)
	p2 = Point(100.0, 0.0)
	print(p1)
	koch(n, p1, p2)
	print(p2)
