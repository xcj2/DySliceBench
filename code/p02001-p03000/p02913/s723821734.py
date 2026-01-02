import sys
import copy

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
	N = II()
	SS = IS()
	ans = 0
	for l in range(N-1):
		i = 1
		j = 0
		S = copy.copy(SS[l:])
		A = [0]*len(S)
		while (i < len(S)):
			while (i+j < len(S) and S[j] == S[i+j]):
				j+=1
			A[i] = j
			if (j == 0):
				i+=1
				continue
			k = 1
			while (i+k < len(S) and k+A[k] < j):
				A[i+k] = A[k]
				k+=1
			i += k
			j -= k
		for m in range(len(S)):
			ans = max(ans, min(m, A[m]))
	print(ans)

main()