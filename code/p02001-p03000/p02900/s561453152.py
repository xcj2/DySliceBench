import sys,math

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
	A,B = MI()
	def gcd(A,B):
		if(B != 0):
			A,B=B,A%B
			return gcd(A,B)
		else:
			return A

	def factorization(n):
		arr = []
		temp = n
		for i in range(2, int(-(-n**0.5//1))+1):
			if temp%i==0:
				cnt=0
				while temp%i==0:
					cnt+=1
					temp //= i
				arr.append([i, cnt])
		if temp!=1:
			arr.append([temp, 1])
		if arr==[]:
			arr.append([n, 1])

		return arr

	A,B=max(A,B),min(A,B)
	gc = gcd(A,B)
	if(gc==1):
		print(1)
	else:
		print(len(factorization(gc))+1)

main()