import sys
input = sys.stdin.readline

def lcs(a, b):
	return a * b // gcd(a,b)

def gcd(a, b):
	if a % b == 0:
		return b
	else:
		return gcd(b, a%b)

def f(a, b, c):
	leftc = a + (c - a % c) % c
	if leftc > b:
		s = 0
	else:
		rightc = b - b % c
		s = (rightc - leftc) // c + 1
	return s

def F(x, c, d):
	res = x
	res -= x // c
	res -= x // d
	res += x // lcs(c, d)
	return res

# a~bまで→　F(b) - F(a-1)と考える（定積分のイメージ）
def main():
	a, b, c, d = map(int, input().strip().split())
	print(F(b, c, d) - F(a-1, c, d))
	# s = f(a, b, c)
	# t = f(a, b, d)
	# u = f(a, b, lcs(c, d))
	# # print(n,s, t, u)
	# print(n - (s + t - u))

if __name__ == '__main__':
	main()
