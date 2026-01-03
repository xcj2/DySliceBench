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
	S = IS()
	S=list(map(int,"".join(S)))
	def dfs(i, total, additional):
		if i==len(S)-1:
			return total+additional
		else:
			return dfs(i+1, total, additional*10+S[i+1]) + dfs(i+1, total+additional, S[i+1])
	print(dfs(0,0,S[0]))


if __name__ == '__main__':
	main()