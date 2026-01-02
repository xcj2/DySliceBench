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
	N,M = MI()
	dp = [float("inf")] * (2**N)
	dp[0] = 0
	for _ in range(M):
		a,b = MI()
		cc = LI()
		state = 0
		for c in cc:
			c -= 1
			state += (1 << c)
		for i in range(2**N):
			if(dp[i]!=float("inf")):
				dp[i|state] = min(dp[i|state], dp[i]+a)
	if(dp[-1]!=float("inf")):
		print(dp[-1])
	else:
		print(-1)


main()