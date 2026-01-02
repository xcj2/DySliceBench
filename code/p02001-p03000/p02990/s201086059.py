N, K = map(int, input().strip().split())
M = 10 ** 9 + 7

def calc_rev(n, law):
	if n == 1:
		return 1
	
	pre_r = law
	pre_x = 0
	pre_y = 1
	cur_r = n
	cur_x = 1
	cur_y = 0
	
	while True:
		d = pre_r // cur_r
		r = pre_r % cur_r
		
		nxt_r = r
		nxt_x = pre_x - d * cur_x
		nxt_y = pre_y - d * cur_y
		
		if nxt_r == 1:
			ret = nxt_x
			while ret < 0:
				ret += law;
			return ret;
		elif nxt_r == 0:
			return None
		
		pre_r = cur_r;
		pre_x = cur_x;
		pre_y = cur_y;
		cur_r = nxt_r;
		cur_x = nxt_x;
		cur_y = nxt_y;

def C(n, m):
	result = 1
	k = m
	while k > 0:
		result = (result * n) % M
		n -= 1
		k -= 1
	
	denom = 1
	while m > 1:
		denom = (denom * m) % M
		m -= 1
	return (result * calc_rev(denom, M)) % M

def factorial(n):
	result = 1
	while n > 1:
		result = (result * n) % M
		n -= 1
	return result

def factorial2(n, m):
	result = 1
	while n > m:
		result = (result * n) % M
		n -= 1
	return result

for i in range(1, K + 1):
	
	if i - 1 <= N - K:
		c1 = C(K - 1, i - 1)
		
		x1 = N - K - (i - 1)
		x2 = i + 1 - 1
		if x1 > x2:
			c2 = factorial2(x1 + x2, x1) * calc_rev(factorial(x2), M)
		else:
			c2 = factorial2(x1 + x2, x2) * calc_rev(factorial(x1), M)
		
#		print(c1, c2)
	
		print((c1 * c2) % M)
	else:
		print(0)



