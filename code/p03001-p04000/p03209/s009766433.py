import sys
sys.setrecursionlimit(10**9)

n,x = map(int,input().split())

def f(n):
	if n == 0:
		return 1
	return 2 * f(n-1) + 3

def f2(n):
	if n == 0:
		return 'P'
	return 'B' + f2(n-1) + 'P' + f2(n-1) + 'B'

def p(n):
	if n == 0:
		return 1
	return 2 * p(n-1) + 1

num = f(n)

ans = 0
while True:
	if num < 10 ** 5:
		break
	tmp = num // 2 + 1

	if x > tmp:
		ans += p(n) // 2 + 1
		x -= tmp
		num -= tmp + 1
	elif x < tmp:
		num -= tmp + 1
		x -= 1
	else:
		print(p(n-1)+1)
		sys.exit()
	n -= 1

string = f2(n)
if len(string) <= x:
	print(p(n)+ans)
else:
	for i in range(x):
		if string[i] == 'P':
			ans += 1
	print(ans)
