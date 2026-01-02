def inp():
	global n
	n = int(input())
	return n
def strinp():
	l = 0
	s = list(input())
	for i in s:
		if i == '.':
			l += 1
		else:
			c = i
	return [l,c]
def calc(p):
	global f
	l = f[p][0]
	c = f[p][1]
	p += 1
	if c == '+':
		ans = 0
		for i in range(p,n):
			if f[i][0] == l:
				break
			elif f[i][0] == l+1:
				ans += calc(i)
	elif c == '*':
		ans = 1
		for i in range(p,n):
			if f[i][0] == l:
				break
			elif f[i][0] == l+1:
				ans *= calc(i)
	else:
		ans = int(c)
	return ans

while inp() > 0:
	f = []
	for i in range(n):
		f.append(strinp())
	print(calc(0))


