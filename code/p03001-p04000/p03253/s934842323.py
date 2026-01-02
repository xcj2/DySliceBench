import sys
input = sys.stdin.readline

N, M = (int(i) for i in input().split())

def soin(N):
	res = []
	i = 2
	while i < round(N**(1/2)) + 3:
		if N%i == 0:
			res.append(i)
			N = N//i
			i = 2
		else:
			i += 1
	if N != 1:
		res.append(N)
	return res

def power(a, b):
	if b == 0:
		return 0
	elif b == 1:
		return a % 1000000007
	elif b % 2 == 0:
		return (power(a, b//2) ** 2) % 1000000007
	else:
		return (power(a, b//2) ** 2 * a) % 1000000007

def divide(a, b):
	return (a * power(b, 1000000005)) % 1000000007

def combination(a, b):
	res = 1
	for i in range(b):
		res *= a - i
		res = res % 1000000007
	for i in range(b):
		res = divide(res, i+1)
	return res
if M == 1:
	res = 1
else:
	L = soin(M)
	cc = 1
	res = 1
	for i in range(len(L) -1):
		if L[i] == L[i+1]:
			cc += 1
		else:
			res *= combination(N + cc -1, cc)
			res = res % 1000000007
			cc = 1
	res *= combination(N+cc -1, cc)
	res = res % 1000000007
print(res)