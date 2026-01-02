EPS = 1e-4


#外積
def OuterProduct(one, two):
	tmp = one.conjugate() * two
	return tmp.imag

#内積
def InnerProduct(one, two):
	tmp = one.conjugate() * two
	return tmp.real

#点が直線上にあるか
def IsOnLine(point, begin, end):
	return abs(OuterProduct(begin-point, end-point)) <= EPS

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

#線分どうし交叉
def Intersect_SS(b1, e1, b2, e2):
	if (CCW(b1, e1, b2) != CCW(b1, e1, e2)) and (CCW(b2, e2, b1) != CCW(b2, e2, e1)):
		return True
	else:
		return False

def solve(a, b, c, d):
	if IsOnSegment(a, c, d) or IsOnSegment(b, c, d) or IsOnSegment(c, a, b) or IsOnSegment(d, a, b):
		return 1
	elif abs(OuterProduct(b-a, d-c)) <= EPS:
		return 0
	elif Intersect_SS(a, b, c, d):
		return 1
	else:
		return 0

n = int(input())
for _ in range(n):
	pp = list(map(int, input().split()))
	p = [complex(pp[i], pp[i+1]) for i in range(0, 8, 2)]
	print(solve(p[0], p[1], p[2], p[3]))
