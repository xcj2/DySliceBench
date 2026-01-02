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
	N,T = MI()
	max_T = -1
	dish = []
	for i in range(N):
		A,B = MI()
		dish.append([A,B])
		dish.sort(key=lambda x : x[0])
		max_T = max(max_T, A)

	dp=[-1 for _ in range(T+max_T)]
	dp[0] = 0
	for i in range(N):
		for j in range(T-1, -1, -1):
			if(dp[j]>=0):
				dp[j+dish[i][0]] = max(dp[j+dish[i][0]], dp[j]+dish[i][1])
	print(max(dp))
main()