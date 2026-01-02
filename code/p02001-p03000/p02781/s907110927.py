import math

def comb(n, r):
	if n <= r:
		return 1
	else:
		return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def perm(n, r):
	if n <= r:
		return math.factorial(n)
	else:
		return math.factorial(n) // (math.factorial(n - r))
	
N = int(input())
K = int(input())
N_str = str(N)
N_keta = len(N_str)
N_f = int(N_str[0])

def K1(a):
	a_str = str(a)
	a_keta = len(a_str)
	a_f = int(a_str[0])
	return a_f + (a_keta-1)*9

def K2(a):
	a_str = str(a)
	a_keta = len(a_str)
	a_f = int(a_str[0])
	if a_keta < 2:
		return 0
	else:
		a_under1 = int(a_str[1:])
		a_list = [9*9*i for i in range(1, a_keta-1)]
		return (a_f-1)*9*(a_keta-1) + K1(a_under1) + sum(a_list)

if K == 1:	
	print(K1(N))

elif K == 2:
	print(K2(N))

elif K == 3:
	if N_keta < 3:
		print(0)
	else:
		N_under1 = int(N_str[1:])
		N_list = [9*9*9*comb(i, 2) for i in range(2, N_keta-1)]
		print(K2(N_under1) + (N_f-1)*9*9*comb(N_keta-1, 2) + sum(N_list))

