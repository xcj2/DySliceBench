import cmath
EPS = 1e-4

#外積
def OuterProduct(one, two):
	tmp = one.conjugate() * two
	return tmp.imag

#内積
def InnerProduct(one, two):
	tmp = one.conjugate() * two
	return tmp.real

#点が線分上にあるか
def IsOnSegment(point, begin, end):
	if abs(OuterProduct(begin-point, end-point)) <= EPS and InnerProduct(begin-point, end-point) <= EPS:
		return True
	else:
		return False

#3点が反時計回りか
#一直線上のときの例外処理できていない→とりあえずF
def CCW(p, q, r):
	one, two = q-p, r-q
	if OuterProduct(one, two) > -EPS:
		return True
	else:
		return False

def solve(p, q, r):
	if abs(OuterProduct(q-r, p-r)) <= EPS:
		if InnerProduct(q-r, p-r) <= EPS:
			return "ON_SEGMENT"
		elif abs(p-r) < abs(q-r):
			return "ONLINE_BACK"
		else:
			return "ONLINE_FRONT"
	elif CCW(p, q, r):
		return "COUNTER_CLOCKWISE"
	else:
		return "CLOCKWISE"

a, b, c, d = map(int, input().split())
p, q = complex(a, b), complex(c, d)
n = int(input())
for _ in range(n):
	x, y = map(int, input().split())
	r = complex(x, y)
	print(solve(p, q, r))
