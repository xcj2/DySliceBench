import sys
def input():
	return sys.stdin.readline()[:-1]

n, q = map(int, input().split())
s = input()
Qs = [input().split() for _ in range(q)]

def calc_l(x):
	for i in range(q):
		if Qs[i][0] == s[x]:
			if Qs[i][1] == "L":
				x -= 1
			else:
				x += 1
		if x < 0:
			return True
		if x > n-1:
			return False
	return False

def calc_r(x):
	for i in range(q):
		if Qs[i][0] == s[x]:
			if Qs[i][1] == "L":
				x -= 1
			else:
				x += 1
		if x > n-1:
			return True
		if x < 0:
			return False
	return False

if calc_l(0):
	l_ok = 0
	l_ng = n
	while l_ng - l_ok > 1:
		left = (l_ok + l_ng) // 2
		if calc_l(left):
			l_ok = left
		else:
			l_ng = left
else:
	l_ok = -1

if calc_r(n-1):
	r_ok = n-1
	r_ng = -1
	while r_ok - r_ng > 1:
		right = (r_ok + r_ng) // 2
		if calc_r(right):
			r_ok = right
		else:
			r_ng = right
		#print(r_ok, r_ng)
	if calc_r(r_ng):
		r_ok = r_ng
else:
	r_ok = n

#print(l_ok, r_ok)
print(r_ok - l_ok - 1)