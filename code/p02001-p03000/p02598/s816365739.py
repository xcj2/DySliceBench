N, K = map(int, input().split())

A_list = list(map(int, input().split()))

# search smallest i such that f(i) == True
def auto_bisearch_smallest(f, s = None):
	if s == None:
		s = 0
		w = -1
		while f(s) == True:
			s = w
			w *= 2
	e = s
	w = 1
	while f(e) == False:
		e = s + w
		w *= 2
	
	return bisearch_smallest(f, s, e + 1)

# search smallest i ( s <= i < e ) such that f(i) == True
def bisearch_smallest(f, s, e = None):
	if e == None:
		e = s - 1
		s = 0
	else:
		e -= 1
	
	while s < e:
		m = (s + e) // 2
		if f(m):
			e = m
		else:
			s = m + 1
	
	if s == e and f(s):
		return s
	else:
		return -1

def calc(length):
	count = 0
	for a in A_list:
		if a > length:
			if a % length == 0:
				count += (a // length) - 1
			else:
				count += a // length
	return count

print(auto_bisearch_smallest(lambda length: calc(length) <= K, 1))
