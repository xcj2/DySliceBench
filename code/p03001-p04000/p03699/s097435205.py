import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LII(rows_number): return [II() for _ in range(rows_number)]
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]

def main():
	N = II()
	S = LII(N)

	total_S = sum(S)
	S.sort()
	if(total_S % 10 == 0):
		i = 0
		for i in range(N):
			f = False
			if(S[i]%10!=0): 
				print(total_S-S[i])
				f=True
				break
		if(f==False):print(0)
	else:
		print(total_S)

main()