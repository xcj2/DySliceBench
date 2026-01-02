import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def IS(): return sys.stdin.readline()[:-1]
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LII(rows_number): return [II() for _ in range(rows_number)]
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]

def main():
	N,K = MI()
	A = LI();A.sort();
	F = LI();F.sort(reverse=True);
	upper_X = -1
	for i in range(N):
		upper_X = max(A[i]*F[i], upper_X)


	def BinarySearch(upper_X, lower_X):
		X = upper_X//2 
		candidate = upper_X
		while upper_X > lower_X:
			deduct = 0
			for i in range(N):
				n = A[i]-X//F[i]
				deduct += n if n>=1 else 0
			if(K < deduct):
				lower_X = X
				if(upper_X - lower_X) <= 1: break
			else:
				candidate = X
				upper_X = X
			X = (lower_X+upper_X)//2
		return candidate

	print(BinarySearch(upper_X,0))


main()