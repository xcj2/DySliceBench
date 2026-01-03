# encoding:utf-8
import math

def main():
	N, P = list(map(int, input().split()))
	biscuits = list(map(int, input().split()))

	n_odd = sum([x % 2 for x in biscuits])
	n_even = N - n_odd

	out = calcNPtrn_odd(n_odd, P) * calcNPtrn_even(n_even)
	print(out)
	
def calcComb(n, m):
	return(math.factorial(n)/math.factorial(m)/math.factorial(n-m))

def calcNPtrn_odd(n, is_odd):
	if n == 0:
		if is_odd == 1:
			return(0)
		else:
			return(1)

	count = 0
	if is_odd == 1:
		for i in range(1, n + 1, 2):
			count += calcComb(n, i)
	else:
		for i in range(0, n + 1, 2):
			count += calcComb(n, i)

	return(int(count))

def calcNPtrn_even(n):
	if n == 0:
		return(1)

	count = 1
	for i in range(1, n + 1):
		count += calcComb(n, i)
	return(int(count))

if __name__ == '__main__':
	main()