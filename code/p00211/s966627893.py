# AOJ 0211: Jogging
# Python3 2018.6.25 bal4u

def lcm(a, b):
	return a // gcd(a, b) * b

def gcd(a, b):
	while b != 0:
		r = a % b
		a, b = b, r
	return a

def ngcd(n, a):  # aが整数のリスト
	if n == 1: return a[0]
	g = gcd(a[0], a[1]);
	for i in range(2, n):
		if g == 1: break
		g = gcd(g, a[i])
	return g;

def nlcm(n, a):  # aが整数のリスト
	if n == 1: return a[0];
	g = gcd(a[0], a[1]);
	c = a[0] //g *a[1]
	for i in range(2, n):
		g = gcd(c, a[i])
		c = c //g * a[i]
	return c

while True:
	n = int(input())
	if n == 0: break
	d, v = [], []
	for i in range(n):
		a, b = map(int, input().split())
		g = gcd(a, b)
		a //= g
		b //= g
		d.append(a)
		v.append(b)
	g = nlcm(n, d);
	for i in range(n): d[i] = (g//d[i])*v[i]
	g = ngcd(n, d)
	for i in range(n): print(d[i]//g)
