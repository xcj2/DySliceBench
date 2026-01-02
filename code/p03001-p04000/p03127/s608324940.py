import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def chkprint(a):
	a_name = ''
	for k, v in globals().items():
		if id(v) == id(a):
			a_name = k
			break
	print(a_name+' = '+str(a), file=sys.stderr)

def mt(f):
	import time
	def wrap(*args, **kwargs):
		s = time.time()
		ret = f(*args, **kwargs)
		e = time.time()
		print(e - s, 'sec', file=sys.stderr)
		return ret
	return wrap

@mt
def slv(N, A):
	flag = True
	while len(A) > 1:
		m = min(A)
		A = [a % m for a in A if a % m != 0]
		A.append(m)
		print(A, file=sys.stderr)
	return m


N = int(input())
A = [int(i) for i in input().split()]
'''
N = 5
A = [13, 5, 18, 100000000]
'''
print(slv(N, A))