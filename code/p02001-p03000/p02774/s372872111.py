import sys
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 10**9 + 7

def comb(n, k):
	p, q = 1, 1
	for i in range(1, k+1):
		p = p * (n-i+1)
		q = q * i
	return p // q

def binsearch(l, r, f):
	while r - l > 1:
		c = (r + l) // 2
		if f(c):
			r = c
		else:
			l = c
	return r

N, K = rl()
A = rl()

pos = 0
neg = 0
zero = 0
Ap = []
An = []
for a in A:
	if a > 0:
		pos += 1
		Ap.append(a)
	elif a < 0:
		neg += 1
		An.append(a)
	else:
		zero += 1
Ap.sort()
An.sort()
n_pos = comb(pos, 2) + comb(neg, 2)
n_neg = pos * neg
n_zero = zero*(N-zero) + comb(zero, 2)

def num_gt(A, x):
	j = len(A) - 1
	cnt = 0
	for i in range(len(A)):
		while i < j and A[i] * A[j] > x:
			j -= 1
		if i >= j:
			break
		cnt += max(j - i, 0)
	return cnt

def num_gt2(A, B, x):
	j = len(B) - 1
	cnt = 0
	for i in reversed(range(len(A))):
		while j >= 0 and A[i] * B[j] > x:
			j -= 1
		if j < 0:
			break
		cnt += max(j+1, 0)
	return cnt

def check_plus(x):
	cnt = n_neg + n_zero
	cnt += num_gt(Ap, x)
	cnt += num_gt(list(reversed(An)), x)
	return cnt >= K

def check_minus(x):
	cnt = num_gt2(Ap, An, x)
	return cnt >= K

ans = 0
if K <= n_neg:
	l = An[0] * Ap[-1] - 1
	r = 0
	ans = binsearch(l, r, check_minus)
elif K <= n_neg + n_zero:
	ans = 0
else:
	l = 0
	r = 1
	if len(Ap) >= 2:
		r = max(r, Ap[-1] * Ap[-2]) + 1
	if len(An) >= 2:
		r = max(r, An[0] * An[1]) + 1
	ans = binsearch(l, r, check_plus)
print(ans)