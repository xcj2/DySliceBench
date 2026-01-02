import time
MOD =  1000000007
MOD2 = 1000000005
MAX = 100001

facs = [1 for _ in range(MAX)]
inv = [1 for _ in range(MAX)]


for i in range(1, MAX):
	facs[i] = (facs[i-1] * i) % MOD

for i in range(1, MAX):
	inv[i] = pow(facs[i], MOD2, MOD)


def get_facs(x):
	return facs[x]


def get_inv(x):
	return inv[x]

def choose(n, k):

	if k==0 or n==k:
		return 1
	if n==0:
		return 0
	if k>n:
		return 0
	r = (get_facs(n)*get_inv(k)) % MOD
	r = (r*get_inv(n-k)) % MOD
	return r



def main():
	N, K = map(int, input().split())
	numbers = sorted(map(int, input().split()))
	if K==1:
		return 0
	if K==N:
		return abs(numbers[0] - numbers[-1])

	score = 0
	for i, x in enumerate(numbers):
		score += ((choose(i, K-1) - choose(N-1-i, K-1)) * x)

	return score%MOD
	
	
print(main())
