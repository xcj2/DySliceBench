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

def main():
	A = []
	S = [[False,False,False] for i in range(3)]
	for i in range(3):
		a=LI()
		A.append(a)
	N = II()
	for _ in range(N):
		b = II()
		for i in range(3):
			for j in range(3):
				if(A[i][j]==b):
					S[i][j]=True
	if((S[0][2]==S[1][2]==S[2][2]==True) or(S[0][1]==S[1][1]==S[2][1]==True) or(S[0][0]==S[1][0]==S[2][0]==True) or(S[0][0]==S[0][1]==S[0][2]==True) or (S[1][0]==S[1][1]==S[1][2]==True) or (S[2][0]==S[2][1]==S[2][2]==True) or (S[0][0]==S[1][1]==S[2][2]==True) or (S[2][0]==S[1][1]==S[0][2]==True)):
		print("Yes")
	else:
		print("No")

if __name__ == '__main__':
	main()