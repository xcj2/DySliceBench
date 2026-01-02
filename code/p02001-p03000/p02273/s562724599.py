import sys
import math

def print_point(point):

	print(f"{point[0]:.8f} {point[1]:.8f}")

def koch(n,p1,p2):

	if n == 0:
		return 0

	# Calculate s,t,u from p1,p2
	s = [0,0]
	t = [0,0]
	u = [0,0]
	s[0] = (2 * p1[0] + 1 * p2[0]) / 3
	s[1] = (2 * p1[1] + 1 * p2[1]) / 3
	t[0] = (1 * p1[0] + 2 * p2[0]) / 3
	t[1] = (1 * p1[1] + 2 * p2[1]) / 3
	u[0] = (t[0] - s[0]) * math.cos(math.radians(60)) - (t[1] - s[1]) * math.sin(math.radians(60)) + s[0]
	u[1] = (t[0] - s[0]) * math.sin(math.radians(60)) + (t[1] - s[1]) * math.cos(math.radians(60)) + s[1]
	
	koch(n-1,p1,s)
	print_point(s)
	
	koch(n-1,s,u)
	print_point(u)

	koch(n-1,u,t)
	print_point(t)

	koch(n-1,t,p2)

def test():

	n = int(sys.stdin.readline())
	
	p1 = [0,0]
	p2 = [100,0]

	print_point(p1)
	koch(n,p1,p2)
	print_point(p2)

if __name__ == "__main__":
	test()


