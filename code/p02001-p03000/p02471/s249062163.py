def gcd(a,b):
	if b>a:
		a,b = b,a
	r = a%b
	if r==0:
		return b
	else:
		return gcd(b, a%b)

def solve(a,b):
	if a==1:
		return 1,0
	if b==1:
		return 0,1
	if a>b:
		q = a//b
		r = a%b
		x, y = solve(r,b)
		return x, y-q*x
	if a<b:
		q = b//a
		r = b%a
		x, y = solve(a,r)
		return x-q*y, y

a,b = map(int, input().split())
g = gcd(a,b)
a//=g
b//=g
x, y = solve(a,b)

def p(n):
	return x+b*n
def q(n):
	return y-a*n

def f(n):
	return abs(p(n))+abs(q(n))

if a>b:
	n = y//a
	nn = n 
	m = f(n)
	if f(n-1) < m:
		nn = n-1
		m = f(n-1)
	if f(n+1) < m:
		nn = n+1
		m = f(n+1)
	x = p(nn)
	y = q(nn)
elif a<b:
	n = -x//b
	nn = n 
	m = f(n)
	if f(n-1) < m:
		nn = n-1
		m = f(n-1)
	if f(n+1) < m:
		nn = n+1
		m = f(n+1)
	x = p(nn)
	y = q(nn)
else:
	x = 0
	y = 1

print("{} {}".format(x,y))

