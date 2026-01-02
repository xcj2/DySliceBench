import sys
'''
	??\?????????????????????
'''
_allinput = []
for inp in sys.stdin:
	_allinput += inp.strip().split(" ")
def _input():
	for put in _allinput:
		yield put
_obj = _input();
def __input():
	return _obj.__next__()
def nextInt():
	return int(__input())

def check(lst,L):
	tot = 1
	curSum = 0
	for i in lst:
		if curSum + i <= L:
			curSum += i
		else:
			curSum = i
			tot += 1
	return tot

def solve(lst,m):
	l,r = max(lst), 100000 * 10000
	while l != r:
		mid = int((l+r)/2)
		if check(lst,mid) <= m:
			r = mid
		else:
			l = mid + 1
	return l


n,m = nextInt(),nextInt()
if m > 0 or n > 0:
	lst = [nextInt() for i in range(0,n)]
	print(solve(lst,m))