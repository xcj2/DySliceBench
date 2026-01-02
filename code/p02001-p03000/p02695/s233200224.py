import sys, math
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 10**9 + 7

N, M, Q = rl()
A, B, C, D = [], [], [], []
for i in range(Q):
	a, b, c, d = rl()
	A.append(a-1)
	B.append(b-1)
	C.append(c)
	D.append(d)

def check(nums):
	for i in range(len(nums)-1):
		if nums[i] > nums[i+1]:
			return False
	return True

def f(nums):
	s = 0
	for i in range(Q):
		if nums[B[i]]-nums[A[i]] == C[i]:
			s += D[i]
	return s

nums = [0] * N
def myiter(M, N, i=0):
	if i == N:
		yield nums
		return
	prev = 1
	if i > 0:
		prev = nums[i-1]
	for j in range(prev,M+1):
		nums[i] = j
		for y in myiter(M, N, i+1):
			yield y


ans = 0
for nums in myiter(M, N):
	if check(nums):
		n = f(nums)
		ans = max(ans, n)
print(ans)
