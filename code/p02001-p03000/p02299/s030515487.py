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

def InsidePolygon(point, dots):
	res = 0
	for i in range(len(dots)-1):
		res += cmath.phase((dots[i+1]-point) / (dots[i]-point))
	res += cmath.phase((dots[0]-point) / (dots[-1]-point))
	if abs(res) <= EPS:
		return False
	else:
		return True

n = int(input())
dots = []
for _ in range(n):
	x, y = map(int, input().split())
	dots.append(complex(x, y))
ans = []

def solve(p, dots):
	for i in range(n-1):
		if IsOnSegment(p, dots[i], dots[i+1]):
			return 1
	if IsOnSegment(p, dots[n-1], dots[0]):
		return 1
	if InsidePolygon(p, dots):
		return 2
	else:
		return 0

q = int(input())
for _ in range(q):
	x, y = map(int, input().split())
	p = complex(x, y)
	ans.append(solve(p, dots))

print(*ans, sep="\n")
