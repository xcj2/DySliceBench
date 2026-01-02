M = 10 ** 9 + 7

n, k = map(int, input().split())

# invert
def calc_inverse(n, law):
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

def fact(a):
	n = 1
	
	for i in range(1, a + 1):
		n = (n * i) % M
	
	return n

facts = [None]
facts_i = [None]
f = 1
for i in range(1, n * 2):
	f = (f * i) % M
	facts.append(f)
	facts_i.append(calc_inverse(f, M))

def calc_count(men, room):
	if room == 1:
		return 1
	else:
		return facts[men + room - 1] * calc_inverse(facts[men], M) * calc_inverse(facts[room - 1], M) % M

def c(a, b):
	return facts[a] * facts_i[a - b] * facts_i[b] % M;

if k >= n:
	print(calc_count(n, n))
else:
	
	count = 0
	for i in range(1, k + 1):
#		print(i, ">", c(n, i), calc_count(i, n - i) % M, "=", c(n, i) * calc_count(i, n - i) % M)
		count = (count + c(n, i) * calc_count(i, n - i)) % M
	
	if k > 1:
		count += 1
	
	print(count)
