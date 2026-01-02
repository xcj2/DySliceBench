import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
printV = lambda x: print(*x, sep="\n")
printH = lambda x: print(" ".join(map(str,x)))
def IS(): return sys.stdin.readline()[:-1]
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LII(rows_number): return [II() for _ in range(rows_number)]
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]
mo = 10**9+7

def primes(n):
	is_prime = [True] * (n + 1)
	is_prime[0] = False
	is_prime[1] = False
	for i in range(2, int(n**0.5) + 1):
		if not is_prime[i]:
			continue
		for j in range(i * 2, n + 1, i):
			is_prime[j] = False
	return is_prime

def main():
	x = II()
	ps = primes(2*10**5)
	for i,n in enumerate(ps[x:],x):
		if(n):
			print(i)
			exit()

if __name__ == '__main__':
	main()